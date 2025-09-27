#!/usr/bin/env python3
"""
Startup script that downloads models and then starts the main application.
This ensures models are available before the FastAPI server starts.
"""

import os
import sys
import subprocess
from download_models import main as download_models_main
from utils.logger_config import app_logger as logger

def main():
    """Main startup function."""
    logger.info("🚀 Starting Bangladeshi Bangla TTS Application...")
    
    # Step 1: Download models
    logger.info("📥 Step 1: Downloading models...")
    download_result = download_models_main()
    
    if download_result != 0:
        logger.warning("⚠️ Some models failed to download, but continuing with startup...")
    
    # Step 2: Start the main application
    logger.info("🌟 Step 2: Starting FastAPI server...")
    
    try:
        # Import and run the main application
        from main import app
        import uvicorn
        
        logger.info("✅ All systems ready! Starting server on 0.0.0.0:8000")
        uvicorn.run(app, host="0.0.0.0", port=8000)
        
    except Exception as e:
        logger.error(f"❌ Failed to start application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
