import asyncio
import json
import os
import shutil
import time
import uuid
from contextlib import asynccontextmanager
from typing import Optional

import soundfile as sf
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.websockets import WebSocketState
from pydantic import BaseModel

from utils import TTS, app_logger as logger

# Global variables
TTS_MODEL = None

class TextRequest(BaseModel):
    text: str
    session_id: Optional[str] = None
    model_type: Optional[str] = "finetuned"  # "finetuned" or "pretrained"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the Bangla TTS model on startup."""
    logger.info("---Loading Bangla TTS model---")
    global TTS_MODEL
    
    # Load Bangla TTS model
    TTS_MODEL = TTS()
    
    logger.info("---Bangla TTS model loaded successfully---")
    yield
    logger.info("Shutting down Bangla Text-to-Speech App!")

app = FastAPI(
    title="Bangla Text-to-Speech API",
    description="Convert Bangla text to natural speech using advanced TTS models",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket connections
connected_clients = {}

@app.websocket("/ws/tts")
async def websocket_tts(websocket: WebSocket):
    """WebSocket endpoint for streaming TTS audio."""
    await websocket.accept()
    session_id = str(uuid.uuid4())
    connected_clients[session_id] = websocket
    
    session_data = {
        "topic": "client_id",
        "session_id": session_id
    }
    
    logger.info(f"WebSocket connection established for session: {session_id}")
    await websocket.send_text(json.dumps(session_data))
    
    try:
        while True:
            await websocket.receive_text()  # Keep alive
    except WebSocketDisconnect:
        if session_id in connected_clients:
            del connected_clients[session_id]
        
        # Clean up session audio directory
        folder_path = os.path.join("audio", session_id)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            try:
                shutil.rmtree(folder_path)
                logger.info(f"Deleted folder: {folder_path}")
            except Exception as e:
                logger.warning(f"Error deleting folder {folder_path}: {e}")

@app.get("/models")
async def get_available_models():
    """Get list of available TTS models."""
    return JSONResponse(content={
        "models": TTS_MODEL.get_available_models()
    })

@app.post("/tts")
async def text_to_speech(request: TextRequest):
    """Convert Bangla text to speech using selected model and return audio via WebSocket."""
    if not request.session_id or request.session_id not in connected_clients:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid or missing session_id. Please connect via WebSocket first."}
        )
    
    # Process Bangla text with selected model
    first_chunk_event = asyncio.Event()
    asyncio.create_task(process_bangla_text(
        request.text, 
        request.session_id, 
        first_chunk_event,
        model_type=request.model_type
    ))
    await first_chunk_event.wait()
    
    return JSONResponse(content={
        "message": f"Bangla TTS processing started successfully with {request.model_type} model",
        "session_id": request.session_id,
        "model_type": request.model_type,
        "language": "bn"
    })


async def process_bangla_text(text: str, session_id: str, first_chunk_event=None, model_type="finetuned"):
    """Process Bangla text and stream audio via WebSocket."""
    logger.info(f"Processing Bangla TTS for session {session_id} using {model_type} model")
    start_time = time.time()
    
    if session_id not in connected_clients:
        logger.warning(f"No connected client for session {session_id}")
        return
    
    try:
        # Split text by Bangla sentence delimiter (।)
        chunks = [chunk.strip() for chunk in text.split('।') if chunk.strip()]
        
        queue = asyncio.Queue()
        session_audio_dir = os.path.join("audio", session_id)
        os.makedirs(session_audio_dir, exist_ok=True)
        
        # Start sender task
        sender_task = asyncio.create_task(
            send_audio_in_order(queue, len(chunks), session_id, first_chunk_event)
        )
        
        async def process_chunk(idx, chunk):
            def tts_and_save():
                audio = TTS_MODEL.bangla_tts(
                    text=chunk,
                    model_type=model_type,
                    is_male=False,
                    is_e2e_vits=True,
                )
                filename = os.path.join(session_audio_dir, f"tts_chunk_{idx}_{model_type}.wav")
                sf.write(filename, audio, 22050)
                return filename
            
            filename = await asyncio.to_thread(tts_and_save)
            await queue.put((idx, filename))
            return filename
        
        # Process all chunks concurrently
        await asyncio.gather(*[process_chunk(idx, chunk) for idx, chunk in enumerate(chunks)])
        await sender_task
        
        # Clean up session audio directory
        if os.path.exists(session_audio_dir):
            shutil.rmtree(session_audio_dir)
        
        logger.info(f"Bangla TTS ({model_type}) completed in {time.time() - start_time:.2f}s")
        
    except Exception as e:
        logger.error(f"Error in Bangla TTS processing ({model_type}): {e}")


async def send_audio_in_order(queue, total_chunks, session_id, first_chunk_event=None):
    """Send audio chunks in order via WebSocket."""
    next_to_send = 0
    pending = {}
    
    while next_to_send < total_chunks:
        idx, filename = await queue.get()
        pending[idx] = filename
        
        while next_to_send in pending:
            filename = pending[next_to_send]
            if session_id in connected_clients and connected_clients[session_id].application_state == WebSocketState.CONNECTED:
                with open(filename, "rb") as f:
                    audio_bytes = f.read()
                    await connected_clients[session_id].send_bytes(audio_bytes)
                
                # Signal after sending the first chunk
                if next_to_send == 0 and first_chunk_event is not None and not first_chunk_event.is_set():
                    first_chunk_event.set()
                
                logger.info(f"Sent audio chunk {next_to_send} for session {session_id}")
                os.remove(filename)
            
            next_to_send += 1

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "Bangla Text-to-Speech API is running"}

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Bangla Text-to-Speech Model Comparison API",
        "version": "2.0.0",
        "description": "Compare fine-tuned and pre-trained Bangla TTS models",
        "endpoints": {
            "websocket": "/ws/tts",
            "models": "/models",
            "tts": "/tts",
            "compare": "/compare",
            "health": "/health"
        },
        "supported_language": "bn (Bangla)",
        "available_models": ["finetuned", "pretrained"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
