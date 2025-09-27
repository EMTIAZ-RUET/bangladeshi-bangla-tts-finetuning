# বাংলা টেক্সট টু স্পিচ অ্যাপ (Bangla Text-to-Speech App)

A modern web application that converts Bangla text to natural speech using advanced TTS models.

## Features

- **বাংলা TTS**: Uses a fine-tuned VITS model for high-quality Bangla speech synthesis
- **Real-time Streaming**: Audio streams in real-time via WebSocket connections
- **Modern UI**: Beautiful, responsive React interface with Tailwind CSS in Bangla
- **Bangla Language Support**: Dedicated support for Bangla text processing
- **Sample Texts**: Pre-loaded Bangla sample texts for quick testing
- **Text Normalization**: Automatic Bangla text normalization and number conversion

## Architecture

### Backend (FastAPI)
- **FastAPI**: Modern Python web framework
- **WebSocket**: Real-time audio streaming
- **TTS Model**: Custom VITS model from Hugging Face for Bangla
- **Audio Processing**: Real-time Bangla audio generation and streaming
- **Text Processing**: Bangla text normalization and number conversion

### Frontend (React + TypeScript)
- **React 18**: Modern React with hooks
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS framework
- **Radix UI**: Accessible UI components
- **WebSocket Client**: Real-time audio playback
- **Bangla UI**: Complete interface in Bangla language

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
```

5. (Optional) Add your Deepgram API key to `.env` for English TTS:
```
DEEPGRAM_API_KEY=your_deepgram_api_key_here
```

6. Run the backend server:
```bash
python main.py
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Usage

1. Open your browser and go to `http://localhost:3000`
2. Enter Bangla text in the textarea or use sample texts
3. Click "কণ্ঠস্বরে রূপান্তর করুন" (Convert to Speech) to generate audio
4. Audio will stream automatically through your speakers

## API Endpoints

### WebSocket
- `ws://localhost:8000/ws/tts` - WebSocket connection for audio streaming

### REST API
- `POST /tts` - Convert Bangla text to speech
- `GET /health` - Health check
- `GET /` - API information

## Dependencies

### Backend
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `torch` - PyTorch for ML models
- `tts` - Coqui TTS library
- `deepgram-sdk` - Deepgram API client
- `soundfile` - Audio file handling

### Frontend
- `react` - UI library
- `typescript` - Type safety
- `tailwindcss` - CSS framework
- `@radix-ui/*` - UI components
- `lucide-react` - Icons

## Models

### Bangla TTS
- **Model**: VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech)
- **Source**: Hugging Face (`AIML-BS23/vits-female-finetuned-quantized`)
- **Features**: 
  - High-quality female voice
  - Bangla text normalization
  - English to Bangla digit conversion
  - Bangla number pronunciation
  - Sentence-wise audio generation

## Troubleshooting

### Common Issues

1. **WebSocket Connection Failed**
   - Ensure backend is running on port 8000
   - Check firewall settings

2. **Audio Not Playing**
   - Check browser audio permissions
   - Ensure speakers/headphones are connected
   - Try refreshing the page

3. **Bangla TTS Not Working**
   - Model will download automatically on first use
   - Ensure stable internet connection for model download
   - Check available disk space (model is ~100MB)
   - Verify CUDA availability for GPU acceleration (24GB VRAM recommended)

## Development

### Improving Bangla TTS
1. Fine-tune the VITS model with more Bangla data
2. Add more Bangla sample texts
3. Improve text normalization rules
4. Add voice selection options (male/female)

### Customizing UI
- Modify `frontend/src/components/TextToSpeechApp.tsx`
- Update styles in `frontend/src/index.css`
- Add new components in `frontend/src/components/ui/`

## License

This project is for educational and demonstration purposes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues and questions, please create an issue in the repository.
