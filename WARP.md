# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Bangladeshi Bangla Text-to-Speech (TTS) fine-tuning project that demonstrates dramatic improvements through systematic model fine-tuning. The project focuses on solving specific pronunciation, tone, and naturalness issues in Bangla TTS synthesis, with audio evidence provided for each improvement.

**Key Achievement**: The project transforms robotic, problematic base model output into natural, human-like speech through VITS model fine-tuning, addressing 7 critical TTS issues with before/after audio comparisons.

## Common Development Commands

### Environment Setup
```bash
# Install core TTS dependencies
pip install TTS librosa soundfile numpy scipy

# For training on Kaggle (as used in the project)
pip install torch torchaudio transformers
```

### Data Preprocessing Pipeline
```bash
# Run text normalization on metadata files
python "03-Data Pipeline Development/data-preprocessing/text_normalization.py"

# Clean and preprocess audio files
python "03-Data Pipeline Development/data-preprocessing/audio_cleaning.py"

# Validate dataset quality
python "03-Data Pipeline Development/data-preprocessing/dataset_quality_checker.py"

# Generate synthetic audio (when needed)
python "03-Data Pipeline Development/data-preprocessing/synthetic_audio_generation.py"
```

### Training and Fine-tuning
```bash
# Execute TTS training on Kaggle
python "04-Finetuning Strategy & Experiments/01-finetuning-pipeline/kaggle_tts_training.py"

# Training command structure (as used in Kaggle script):
CUDA_VISIBLE_DEVICES="0" python /path/to/train_tts.py \
    --config_path /path/to/config.json \
    --restore_path /path/to/model_file.pth
```

### Audio Quality Verification
```bash
# Listen to before/after audio samples in the "Proble resolved by finetuning/" directory
# Each problem category contains:
# - base_model.wav (original problematic output)
# - fine_tuned.wav (improved output after fine-tuning)
# - sentence.txt (text used for comparison)
```

## High-Level Architecture

### Phase-Based Structure
The project follows a systematic 6-phase approach:

1. **Research & Environment Setup** (`01-Research & Environment Setup/`)
   - Model selection analysis (VITS vs XTTS decision)
   - Architecture investigations and environment configuration

2. **Data Research & Acquisition** (`02-Data Research & Acquisition/`)
   - Dataset collection from OpenSLR 53/54, Common Voice Bangla
   - Quality assessment and accent investigation

3. **Data Pipeline Development** (`03-Data Pipeline Development/`)
   - Core preprocessing scripts for audio cleaning and text normalization
   - Dataset quality validation and synthetic data generation
   - LJSpeech format conversion for TTS training

4. **Fine-tuning Strategy & Experiments** (`04-Finetuning Strategy & Experiments/`)
   - Kaggle-based training pipeline using VITS architecture
   - Training process execution and result analysis
   - Comprehensive training logs and model checkpoints

5. **Optimization** (`05-Optimization/`)
   - Model quantization, pruning, and compression techniques
   - Inference optimization through caching and streaming

6. **Final Evaluation & Documentation** (`06-Final Evaluation & Documentation/`)
   - Comprehensive model evaluation and deployment planning

### Core Technical Components

**Model Architecture**: VITS (chosen over XTTS due to GPU constraints)
- Target sample rate: 22050 Hz
- Training platform: Kaggle with Tesla T4 GPUs
- Language: Bangladeshi Bangla (bn-Bangladesh)

**Data Processing Pipeline**:
- Audio preprocessing: Resampling, silence trimming, noise filtering
- Text normalization: Number-to-word conversion, Unicode standardization
- Quality validation: Character validation, audio quality checks

**Training Infrastructure**:
- Platform: Kaggle cloud environment
- GPU configuration: CUDA-enabled Tesla T4 (15GB VRAM)
- Training framework: Coqui TTS library with PyTorch backend

## Project-Specific Context

### Model Selection Rationale
VITS was chosen over XTTS due to practical constraints:
- XTTS requires 3.85k hours of data and A100 GPUs with 80GB VRAM
- VITS can be fine-tuned on Kaggle's 15GB GPU environment
- Pre-trained Bangla VITS checkpoints are available, enabling rapid adaptation

### Audio Evidence Approach
Unlike typical TTS projects that focus on metrics, this project provides actual audio comparisons:
- **7 problem categories** with before/after audio evidence
- Each category demonstrates specific improvements (pronunciation, tone, naturalness, etc.)
- Audio files located in `Proble resolved by finetuning/` directory

### Data Sources and Format
- Primary datasets: OpenSLR 53 (Bangladeshi Bangla), OpenSLR 54 (Indian Bengali)
- Format: LJSpeech-style metadata (file_path|raw_text|normalized_text)
- Audio specs: 22.05 kHz sampling rate, mono channel, trimmed to <20 seconds

### Training Configuration
- Platform: Kaggle cloud environment with dataset linking
- Expected datasets: `datahrbnn` (training scripts) and `ttsbnng` (model configs)
- Training timeout: 6 hours maximum per session
- Output storage: `/kaggle/working/` for model checkpoints and logs

## File Organization

- Each phase directory contains relevant `.md` documentation files
- Python scripts are self-contained with inline documentation
- Training logs and results are organized chronologically
- Audio evidence is categorized by problem type with descriptive filenames

This project prioritizes practical implementation and audible proof of improvements over theoretical metrics, making it particularly suitable for demonstration and evaluation of TTS fine-tuning techniques.