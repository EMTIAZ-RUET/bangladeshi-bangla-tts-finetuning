import os
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cache_audio(audio_data, cache_dir="./cache"):
    """
    Cache audio data to a specified directory.

    Args:
        audio_data: The audio data to be cached.
        cache_dir: The directory where the audio data will be cached.

    Returns:
        The path to the cached audio file.
    """
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, f"audio_{int(time.time())}.wav")

    with open(cache_path, "wb") as f:
        f.write(audio_data)

    logger.info(f"Audio cached at: {cache_path}")
    return cache_path

def stream_audio(audio_path):
    """
    Simulate streaming audio from a file.

    Args:
        audio_path: The path to the audio file to be streamed.
    """
    logger.info(f"Streaming audio from: {audio_path}")
    with open(audio_path, "rb") as f:
        while chunk := f.read(1024):
            time.sleep(0.1)  # Simulate network latency
            logger.info(f"Streaming chunk: {len(chunk)} bytes")

if __name__ == "__main__":
    # Example usage
    dummy_audio_data = b"\x00" * 1024  # Simulated audio data
    cached_path = cache_audio(dummy_audio_data)
    stream_audio(cached_path)