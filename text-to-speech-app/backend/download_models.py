#!/usr/bin/env python3
"""
Pre-download script to download all models during Docker build/startup.
This ensures models are available before the main application starts.
"""

import os
import sys
from huggingface_hub import snapshot_download
from utils.logger_config import app_logger as logger

def download_huggingface_model():
    """Download the Hugging Face model."""
    repo_id = "EMTIAZZ/bangladeshi-bangla-tts-vits"
    
    try:
        logger.info(f"🔄 Pre-downloading model from Hugging Face: {repo_id}")
        
        # Download model to cache
        local_dir = snapshot_download(repo_id=repo_id)
        
        # Verify files exist
        model_path = os.path.join(local_dir, "pytorch_model.pth")
        config_path = os.path.join(local_dir, "config.json")
        
        if os.path.exists(model_path) and os.path.exists(config_path):
            logger.info(f"✅ Successfully pre-downloaded model from: {repo_id}")
            logger.info(f"   Model: {model_path}")
            logger.info(f"   Config: {config_path}")
            return True
        else:
            logger.error(f"❌ Model files not found after download")
            return False
            
    except Exception as e:
        logger.error(f"❌ Failed to pre-download model from {repo_id}: {e}")
        return False

def download_coqui_model():
    """Pre-load Coqui TTS model."""
    try:
        logger.info("🔄 Pre-loading Coqui TTS model...")
        from TTS.api import TTS as CoquiTTS
        import time
        
        # This will download the model if not already cached
        # Add timeout and retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                logger.info(f"Attempt {attempt + 1}/{max_retries} to download Coqui model...")
                model = CoquiTTS(model_name="tts_models/bn/custom/vits-female")
                logger.info("✅ Successfully pre-loaded Coqui TTS model")
                return True
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    logger.info("Retrying in 10 seconds...")
                    time.sleep(10)
                else:
                    raise e
        
    except Exception as e:
        logger.error(f"❌ Failed to pre-load Coqui model after {max_retries} attempts: {e}")
        logger.info("💡 Coqui model will be loaded on-demand when requested")
        return False

def main():
    """Main function to download all models."""
    logger.info("🚀 Starting model pre-download process...")
    
    success_count = 0
    total_models = 2
    
    # Download Hugging Face model
    if download_huggingface_model():
        success_count += 1
    
    # Download Coqui model
    if download_coqui_model():
        success_count += 1
    
    logger.info(f"📊 Model download summary: {success_count}/{total_models} models downloaded successfully")
    
    if success_count > 0:
        logger.info("✅ Model pre-download completed successfully!")
        return 0
    else:
        logger.error("❌ No models were downloaded successfully!")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
