#!/usr/bin/env python3
"""
Test script for Hugging Face TTS model
This script tests loading and using your model from Hugging Face Hub
"""

import os
import sys
import soundfile as sf
from utils import TTS
import argparse

def test_huggingface_model(repo_id=None, test_text=None):
    """Test the Hugging Face model loading and inference"""
    
    print("🧪 Testing Bangladeshi Bangla TTS Model from Hugging Face")
    print("=" * 60)
    
    # Default test text
    if not test_text:
        test_text = "আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি। এটি একটি পরীক্ষা।"
    
    print(f"📝 Test text: {test_text}")
    print()
    
    try:
        # Initialize TTS
        print("🔄 Initializing TTS system...")
        tts = TTS()
        
        # Update repo_id if provided
        if repo_id:
            print(f"🔧 Updating repo_id to: {repo_id}")
            tts.available_models["huggingface"]["repo_id"] = repo_id
            # Reload the model with new repo_id
            tts.models = {}
            tts._load_all_models()
        
        # Check available models
        print("📋 Available models:")
        available_models = tts.get_available_models()
        for model_key, model_info in available_models.items():
            status = "✅ Loaded" if model_info["loaded"] else "❌ Failed"
            print(f"  - {model_key}: {model_info['name']} - {status}")
        print()
        
        # Test Hugging Face model
        if not available_models.get("huggingface", {}).get("loaded", False):
            print("❌ Hugging Face model not loaded. Please check:")
            print("  1. Your repo_id is correct")
            print("  2. You have internet connection")
            print("  3. The repository exists and is accessible")
            return False
        
        print("🎵 Generating speech with Hugging Face model...")
        audio = tts.bangla_tts(
            text=test_text,
            model_type="huggingface",
            is_male=False,
            is_e2e_vits=True
        )
        
        # Save test audio
        output_file = "test_huggingface_output.wav"
        sf.write(output_file, audio, 22050)
        
        print(f"✅ Success! Audio saved to: {output_file}")
        print(f"📊 Audio length: {len(audio)/22050:.2f} seconds")
        print(f"📈 Sample rate: 22050 Hz")
        print(f"🔊 Audio shape: {audio.shape}")
        
        # Compare with local model if available
        if available_models.get("finetuned", {}).get("loaded", False):
            print("\n🔄 Comparing with local model...")
            local_audio = tts.bangla_tts(
                text=test_text,
                model_type="finetuned",
                is_male=False,
                is_e2e_vits=True
            )
            
            local_output_file = "test_local_output.wav"
            sf.write(local_output_file, local_audio, 22050)
            
            print(f"💾 Local model audio saved to: {local_output_file}")
            print(f"📊 Local audio length: {len(local_audio)/22050:.2f} seconds")
            
            # Basic comparison
            length_diff = abs(len(audio) - len(local_audio)) / 22050
            print(f"⏱️ Length difference: {length_diff:.2f} seconds")
            
            if length_diff < 1.0:
                print("✅ Models produce similar length audio")
            else:
                print("⚠️ Significant length difference between models")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing Hugging Face model: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check your internet connection")
        print("2. Verify the repo_id is correct")
        print("3. Ensure you have access to the repository")
        print("4. Check if the model files exist in the repository")
        return False

def main():
    parser = argparse.ArgumentParser(description="Test Bangladeshi Bangla TTS model from Hugging Face")
    parser.add_argument("--repo-id", help="Hugging Face repository ID (e.g., username/model-name)")
    parser.add_argument("--text", help="Test text in Bangla", 
                       default="আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি। এটি একটি পরীক্ষা।")
    
    args = parser.parse_args()
    
    success = test_huggingface_model(repo_id=args.repo_id, test_text=args.text)
    
    if success:
        print("\n🎉 Test completed successfully!")
        print("Your Hugging Face model is working correctly.")
    else:
        print("\n❌ Test failed!")
        print("Please check the error messages and troubleshoot.")
        sys.exit(1)

if __name__ == "__main__":
    main()
