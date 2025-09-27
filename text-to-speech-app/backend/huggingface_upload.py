#!/usr/bin/env python3
"""
Hugging Face Model Upload Script for Bangladeshi Bangla TTS Model
This script uploads your fine-tuned VITS model to Hugging Face Hub
"""

import os
import json
import shutil
from pathlib import Path
from huggingface_hub import HfApi, create_repo, upload_folder
from huggingface_hub.utils import RepositoryNotFoundError
import argparse

class HuggingFaceModelUploader:
    def __init__(self, model_name: str, username: str, token: str = None):
        """
        Initialize the uploader
        
        Args:
            model_name: Name for your model repository (e.g., "bangladeshi-bangla-tts-vits")
            username: Your Hugging Face username
            token: Your Hugging Face token (optional if logged in via CLI)
        """
        self.model_name = model_name
        self.username = username
        self.repo_id = f"{username}/{model_name}"
        self.api = HfApi(token=token)
        
        # Paths
        self.model_dir = Path("models/vits-female-finetuned-quantized")
        self.temp_upload_dir = Path("temp_hf_upload")
        
    def prepare_model_files(self):
        """Prepare model files for upload"""
        print("📁 Preparing model files for upload...")
        
        # Create temporary upload directory
        if self.temp_upload_dir.exists():
            shutil.rmtree(self.temp_upload_dir)
        self.temp_upload_dir.mkdir(exist_ok=True)
        
        # Copy model files
        model_file = self.model_dir / "pytorch_model.pth"
        config_file = self.model_dir / "config_finetuned.json"
        
        if not model_file.exists():
            raise FileNotFoundError(f"Model file not found: {model_file}")
        if not config_file.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")
        
        # Copy files to temp directory
        shutil.copy2(model_file, self.temp_upload_dir / "pytorch_model.pth")
        shutil.copy2(config_file, self.temp_upload_dir / "config.json")  # Rename to standard name
        
        print(f"✅ Model files prepared in {self.temp_upload_dir}")
        
    def create_model_card(self):
        """Create a comprehensive model card (README.md)"""
        print("📝 Creating model card...")
        
        model_card_content = f"""---
language:
- bn
license: apache-2.0
tags:
- text-to-speech
- tts
- bangla
- bengali
- vits
- pytorch
- audio
library_name: TTS
pipeline_tag: text-to-speech
---

# Bangladeshi Bangla Text-to-Speech (VITS)

This is a fine-tuned VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech) model for Bangladeshi Bangla text-to-speech synthesis.

## Model Description

- **Language**: Bangla (Bengali) - Bangladeshi variant
- **Architecture**: VITS (Variational Inference Text-to-Speech)
- **Task**: Text-to-Speech (TTS)
- **Training**: Fine-tuned on Bangladeshi Bangla speech data
- **Voice**: Female speaker
- **Sample Rate**: 22050 Hz

## Features

- High-quality Bangla speech synthesis
- Support for Bangladeshi Bangla pronunciation and intonation
- End-to-end neural text-to-speech
- Real-time inference capability
- Proper handling of Bangla numerals and punctuation

## Usage

### Using with TTS Library

```python
import torch
import soundfile as sf
from TTS.api import TTS

# Load the model
tts = TTS(model_path="path/to/pytorch_model.pth", 
          config_path="path/to/config.json")

# Generate speech
text = "আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি।"
audio = tts.tts(text)

# Save audio
sf.write("output.wav", audio, 22050)
```

### Using with Hugging Face Hub

```python
from huggingface_hub import snapshot_download
import torch
import soundfile as sf

# Download model
model_path = snapshot_download(repo_id="{self.repo_id}")

# Load and use the model
# (Add your custom loading code here)
```

## Model Performance

- **Training Epochs**: 100
- **Model Size**: ~997MB
- **Inference Speed**: Real-time capable
- **Audio Quality**: High fidelity speech synthesis

## Training Data

This model was fine-tuned on Bangladeshi Bangla speech data to capture the specific pronunciation, intonation, and linguistic characteristics of Bangladeshi Bengali.

## Limitations

- Optimized for Bangladeshi Bangla variant
- Single female voice
- May not handle out-of-vocabulary words perfectly
- Performance may vary with very long texts

## Technical Details

- **Framework**: PyTorch
- **Architecture**: VITS
- **Sampling Rate**: 22050 Hz
- **Quantization**: Model is quantized for efficient inference

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{{bangladeshi-bangla-tts-vits,
  title={{Bangladeshi Bangla Text-to-Speech using VITS}},
  author={{{self.username}}},
  year={{2024}},
  publisher={{Hugging Face}},
  url={{https://huggingface.co/{self.repo_id}}}
}}
```

## License

This model is released under the Apache 2.0 License.

## Contact

For questions or issues, please open an issue in the repository or contact the author.
"""
        
        with open(self.temp_upload_dir / "README.md", "w", encoding="utf-8") as f:
            f.write(model_card_content)
        
        print("✅ Model card created")
        
    def create_model_requirements(self):
        """Create requirements.txt for the model"""
        print("📋 Creating requirements.txt...")
        
        requirements_content = """torch>=1.9.0
torchaudio>=0.9.0
TTS>=0.22.0
soundfile>=0.12.1
numpy>=1.21.0
huggingface-hub>=0.16.0
bangla>=0.0.2
bnnumerizer>=0.0.2
bnunicodenormalizer>=0.0.7
"""
        
        with open(self.temp_upload_dir / "requirements.txt", "w") as f:
            f.write(requirements_content)
        
        print("✅ Requirements file created")
        
    def create_model_config_metadata(self):
        """Create additional metadata files"""
        print("⚙️ Creating model metadata...")
        
        # Create model info JSON
        model_info = {
            "model_type": "vits",
            "language": "bn",
            "license": "apache-2.0",
            "library_name": "TTS",
            "pipeline_tag": "text-to-speech",
            "tags": ["text-to-speech", "tts", "bangla", "bengali", "vits", "pytorch", "audio"],
            "datasets": ["custom-bangladeshi-bangla"],
            "metrics": ["audio-quality"],
            "model_size": "997MB",
            "sample_rate": 22050,
            "voice_type": "female",
            "training_epochs": 100
        }
        
        with open(self.temp_upload_dir / "model_info.json", "w", encoding="utf-8") as f:
            json.dump(model_info, f, indent=2, ensure_ascii=False)
        
        print("✅ Model metadata created")
        
    def create_repository(self):
        """Create the repository on Hugging Face Hub"""
        print(f"🏗️ Creating repository: {self.repo_id}")
        
        try:
            # Check if repo already exists
            self.api.repo_info(repo_id=self.repo_id)
            print(f"⚠️ Repository {self.repo_id} already exists")
            return True
        except RepositoryNotFoundError:
            # Create new repository
            create_repo(
                repo_id=self.repo_id,
                token=self.api.token,
                repo_type="model",
                private=False,  # Set to True if you want a private repo
                exist_ok=True
            )
            print(f"✅ Repository {self.repo_id} created successfully")
            return True
        except Exception as e:
            print(f"❌ Error creating repository: {e}")
            return False
            
    def upload_model(self):
        """Upload the model to Hugging Face Hub"""
        print(f"🚀 Uploading model to {self.repo_id}...")
        
        try:
            upload_folder(
                folder_path=str(self.temp_upload_dir),
                repo_id=self.repo_id,
                token=self.api.token,
                commit_message="Upload Bangladeshi Bangla TTS VITS model"
            )
            print(f"✅ Model uploaded successfully to https://huggingface.co/{self.repo_id}")
            return True
        except Exception as e:
            print(f"❌ Error uploading model: {e}")
            return False
            
    def cleanup(self):
        """Clean up temporary files"""
        if self.temp_upload_dir.exists():
            shutil.rmtree(self.temp_upload_dir)
            print("🧹 Cleaned up temporary files")
            
    def upload_complete_model(self):
        """Complete model upload process"""
        try:
            print("🚀 Starting Bangladeshi Bangla TTS model upload to Hugging Face...")
            
            # Step 1: Prepare files
            self.prepare_model_files()
            
            # Step 2: Create documentation
            self.create_model_card()
            self.create_model_requirements()
            self.create_model_config_metadata()
            
            # Step 3: Create repository
            if not self.create_repository():
                return False
                
            # Step 4: Upload model
            if not self.upload_model():
                return False
                
            print(f"""
🎉 SUCCESS! Your model has been uploaded to Hugging Face!

📍 Model URL: https://huggingface.co/{self.repo_id}
📚 You can now use your model with:

```python
from huggingface_hub import snapshot_download
model_path = snapshot_download(repo_id="{self.repo_id}")
```

🔧 Next steps:
1. Update your TTS class to support loading from Hugging Face
2. Test the model download and loading
3. Share your model with the community!
            """)
            
            return True
            
        except Exception as e:
            print(f"❌ Upload failed: {e}")
            return False
        finally:
            self.cleanup()

def main():
    parser = argparse.ArgumentParser(description="Upload Bangladeshi Bangla TTS model to Hugging Face")
    parser.add_argument("--model-name", required=True, help="Model repository name (e.g., bangladeshi-bangla-tts-vits)")
    parser.add_argument("--username", required=True, help="Your Hugging Face username")
    parser.add_argument("--token", help="Your Hugging Face token (optional if logged in via CLI)")
    
    args = parser.parse_args()
    
    # Create uploader and upload model
    uploader = HuggingFaceModelUploader(
        model_name=args.model_name,
        username=args.username,
        token=args.token
    )
    
    success = uploader.upload_complete_model()
    
    if success:
        print("\n✅ Model upload completed successfully!")
    else:
        print("\n❌ Model upload failed!")
        exit(1)

if __name__ == "__main__":
    main()
