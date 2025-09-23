"""
Kaggle TTS Training Script for Bangladeshi Bangla TTS Fine-tuning

This script is designed to run on Kaggle's Python environment for training
a Text-to-Speech model using the Coqui TTS library. It leverages Kaggle's
GPU resources and dataset management system.

Environment: Kaggle Python Docker Image
GPU Support: CUDA-enabled training
Libraries: TTS (Coqui), NumPy, Pandas

Usage:
    1. Upload this script to Kaggle as a notebook or script
    2. Ensure input datasets are properly linked
    3. Run the script to start TTS model training
    
Dataset Requirements:
    - Pre-processed audio files in /kaggle/input/
    - Model configuration files (config.json)
    - Pre-trained model checkpoint (model_file.pth)
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
print("=== Kaggle Input Directory Structure ===")
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

print("\n=== Kaggle Environment Information ===")
print(f"Current working directory: {os.getcwd()}")
print(f"Available directories:")
for dir_name in ['/kaggle/input', '/kaggle/working', '/kaggle/temp']:
    if os.path.exists(dir_name):
        print(f"  ✓ {dir_name}")
    else:
        print(f"  ✗ {dir_name} (not found)")

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

print("\n=== Installing TTS Library ===")
# Install TTS library (Coqui TTS) for Text-to-Speech training
import subprocess
import sys

try:
    import TTS
    print("✓ TTS library already installed")
except ImportError:
    print("Installing TTS library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "TTS"])
    print("✓ TTS library installed successfully")

# Import TTS after installation
try:
    from TTS.utils.manage import ModelManager
    from TTS.utils.synthesizer import Synthesizer
    print("✓ TTS imports successful")
except Exception as e:
    print(f"⚠ TTS import warning: {e}")

print("\n=== GPU Configuration ===")
try:
    import torch
    if torch.cuda.is_available():
        print(f"✓ CUDA available - Device count: {torch.cuda.device_count()}")
        print(f"✓ Current device: {torch.cuda.current_device()}")
        print(f"✓ Device name: {torch.cuda.get_device_name()}")
    else:
        print("⚠ CUDA not available - using CPU")
except Exception as e:
    print(f"⚠ GPU check error: {e}")

print("\n=== Dataset Verification ===")
# Check for required dataset paths
dataset_paths = [
    '/kaggle/input/datahrbnn/MyTTSDataset/train_tts.py',
    '/kaggle/input/ttsbnng/transformers/default/1/model/config.json',
    '/kaggle/input/ttsbnng/transformers/default/1/model/model_file.pth'
]

all_paths_exist = True
for path in dataset_paths:
    if os.path.exists(path):
        print(f"✓ Found: {path}")
    else:
        print(f"✗ Missing: {path}")
        all_paths_exist = False

if not all_paths_exist:
    print("\n⚠ Warning: Some required files are missing!")
    print("Please ensure all datasets are properly linked in Kaggle.")
    print("Expected datasets:")
    print("  1. datahrbnn dataset containing MyTTSDataset/train_tts.py")
    print("  2. ttsbnng dataset containing model config and checkpoint")

print("\n=== Starting TTS Training ===")

# Training configuration
training_command = [
    'python', '/kaggle/input/datahrbnn/MyTTSDataset/train_tts.py',
    '--config_path', '/kaggle/input/ttsbnng/transformers/default/1/model/config.json',
    '--restore_path', '/kaggle/input/ttsbnng/transformers/default/1/model/model_file.pth'
]

print(f"Training command: {' '.join(training_command)}")

# Set CUDA device for training
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
print(f"CUDA_VISIBLE_DEVICES set to: {os.environ.get('CUDA_VISIBLE_DEVICES', 'not set')}")

try:
    if all_paths_exist:
        print("\n🚀 Launching TTS training...")
        print("=" * 50)
        
        # Execute the training command
        result = subprocess.run(
            training_command,
            capture_output=True,
            text=True,
            timeout=3600 * 6  # 6 hour timeout
        )
        
        if result.returncode == 0:
            print("✅ Training completed successfully!")
            print("\nTraining output:")
            print(result.stdout)
        else:
            print("❌ Training failed!")
            print(f"Return code: {result.returncode}")
            print(f"Error output: {result.stderr}")
            
    else:
        print("\n⚠ Skipping training due to missing files")
        print("Please check dataset links and try again")
        
except subprocess.TimeoutExpired:
    print("⚠ Training timeout (6 hours) - process terminated")
except Exception as e:
    print(f"❌ Training error: {e}")

print("\n=== Training Session Complete ===")
print("Check /kaggle/working/ for output files and model checkpoints")

# List output files
if os.path.exists('/kaggle/working'):
    working_files = os.listdir('/kaggle/working')
    if working_files:
        print(f"\nGenerated files in /kaggle/working:")
        for file in working_files:
            file_path = os.path.join('/kaggle/working', file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                print(f"  📄 {file} ({size:,} bytes)")
            else:
                print(f"  📁 {file}/")
    else:
        print("\nNo output files generated")