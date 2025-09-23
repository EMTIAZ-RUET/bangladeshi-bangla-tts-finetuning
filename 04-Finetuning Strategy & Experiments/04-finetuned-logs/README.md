# Fine-tuning Training Logs

This directory contains training logs from the Bangladeshi Bangla TTS model fine-tuning experiments.

## Files Overview

### Training Log Files (Markdown)
- **`Finetunelog.md`** - Initial fine-tuning training log with detailed metrics
- **`finetunelog2.md`** - Second fine-tuning session logs  
- **`finetune 4.md`** - Fourth fine-tuning experiment logs
- **`finetune long 3.md`** - Extended third fine-tuning session logs

### Source Files (ODT Format)
- **`Finetunelog.odt`** - Original training log (LibreOffice format)
- **`finetunelog2.odt`** - Original second session log
- **`finetune 4.odt`** - Original fourth experiment log
- **`finetune long 3.odt`** - Original extended third session log

## Log Contents

Each training log contains:
- **Training Environment Setup** - GPU, CPU, memory configuration
- **Model Parameters** - Network architecture details (~83M parameters)
- **Training Metrics** - Loss values, learning rates, gradient norms
- **Evaluation Results** - Performance metrics per epoch
- **Checkpoint Information** - Model saving timestamps and paths

## Key Training Details

- **Model**: VITS (Variational Inference with adversarial learning for end-to-end Text-to-Speech)
- **Hardware**: Single GPU training with mixed precision (fp16)
- **Epochs**: Training for up to 50 epochs
- **Step Range**: Global steps from ~845,000 to ~847,000+
- **Learning Rate**: 0.0002 with scheduling
- **Loss Components**: Discriminator loss, generator loss, KL divergence, feature matching, mel-spectrogram, duration prediction

## Usage

The markdown files (`.md`) are optimized for viewing on GitHub and provide the same content as the original ODT files but in a more accessible format for version control and collaborative review.

## File Conversion

Original ODT files were converted to Markdown using a custom Python script (`odt_to_md.py`) that extracts text content from the OpenDocument format and formats it for better readability in GitHub.

---
*These logs document the fine-tuning process for the Bangladeshi Bangla TTS project, providing detailed insights into model performance and training progression.*