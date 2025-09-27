# Kaggle TTS Training Guide

## Overview

This document describes the **Kaggle TTS Training Script** (`kaggle_tts_training.py`) designed for fine-tuning Bangladeshi Bangla Text-to-Speech models using Kaggle's cloud computing platform.

## 🎯 **Purpose**

The script leverages **Kaggle's GPU resources** and **dataset management system** to train TTS models efficiently without requiring local computational resources. This is particularly valuable for:

- **Resource-limited environments** where local GPU training is not feasible
- **Collaborative development** where multiple team members need access to training results
- **Experiment tracking** with Kaggle's built-in versioning and output management

---

## 🔧 **Technical Architecture**

### **Environment Setup**
- **Base Image**: [Kaggle Python Docker Image](https://github.com/kaggle/docker-python)
- **Python Version**: Python 3.x with pre-installed data science libraries
- **GPU Support**: CUDA-enabled Tesla T4 GPUs (2× 15GB VRAM each)
- **Storage**: 20GB persistent storage in `/kaggle/working/`

### **Key Libraries**
```python
- numpy: Linear algebra and numerical computations
- pandas: Data processing and CSV file I/O
- TTS: Coqui TTS library for Text-to-Speech training
- torch: PyTorch deep learning framework
- subprocess: System command execution
```

---

## 📁 **File Structure**

### **Input Directory (`/kaggle/input/`)**
```
/kaggle/input/
├── datahrbnn/
│   └── MyTTSDataset/
│       └── train_tts.py          # Main training script
├── ttsbnng/
│   └── transformers/
│       └── default/
│           └── 1/
│               └── model/
│                   ├── config.json       # Model configuration
│                   └── model_file.pth    # Pre-trained checkpoint
```

### **Output Directory (`/kaggle/working/`)**
- **Model checkpoints**: Saved during training
- **Training logs**: Performance metrics and loss curves
- **Configuration files**: Modified training parameters
- **Generated audio**: Sample outputs for validation

---

## 🚀 **Script Functionality**

### **1. Environment Verification**
```python
# Checks Kaggle directory structure
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
```

**Features:**
- ✅ Lists all available input files
- ✅ Verifies directory accessibility
- ✅ Reports environment configuration

### **2. TTS Library Installation**
```python
pip install TTS
```

**Process:**
- ✅ Checks if TTS library is already installed
- ✅ Installs Coqui TTS if not present
- ✅ Verifies successful import of TTS modules

### **3. GPU Configuration**
```python
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
```

**Features:**
- ✅ Detects available CUDA devices
- ✅ Reports GPU specifications
- ✅ Sets device visibility for training

### **4. Dataset Validation**
```python
dataset_paths = [
    '/kaggle/input/datahrbnn/MyTTSDataset/train_tts.py',
    '/kaggle/input/ttsbnng/transformers/default/1/model/config.json',
    '/kaggle/input/ttsbnng/transformers/default/1/model/model_file.pth'
]
```

**Validation:**
- ✅ Verifies presence of training script
- ✅ Checks model configuration file
- ✅ Confirms pre-trained model checkpoint
- ⚠️ Reports missing files with clear error messages

### **5. Training Execution**
```bash
CUDA_VISIBLE_DEVICES="0" python /kaggle/input/datahrbnn/MyTTSDataset/train_tts.py \
    --config_path /kaggle/input/ttsbnng/transformers/default/1/model/config.json \
    --restore_path /kaggle/input/ttsbnng/transformers/default/1/model/model_file.pth
```

**Configuration:**
- **GPU Assignment**: Uses GPU 0 for training
- **Configuration Path**: Points to model architecture settings
- **Restore Path**: Loads pre-trained weights for fine-tuning
- **Timeout**: 6-hour maximum training duration

---

## 📊 **Training Parameters**

### **Hardware Resources**
| Resource | Specification |
|----------|---------------|
| **GPU** | 2× NVIDIA Tesla T4 (15GB each) |
| **RAM** | 30GB system memory |
| **Storage** | 20GB persistent + temporary |
| **Session Time** | 12 hours maximum |

### **TTS Model Configuration**
- **Architecture**: Specified in `config.json`
- **Sample Rate**: 22050 Hz (compatible with preprocessing)
- **Language**: Bangladeshi Bangla (`bn-Bangladesh`)
- **Training Type**: Fine-tuning from pre-trained checkpoint

---

## 🛠️ **Usage Instructions**

### **Step 1: Prepare Datasets**
1. **Upload Training Data**: Add your preprocessed audio and text data
2. **Link Datasets**: Connect the `datahrbnn` and `ttsbnng` datasets in Kaggle
3. **Verify Paths**: Ensure file paths match the script expectations

### **Step 2: Configure Training**
```json
// Modify config.json for your specific requirements
{
    "model": "vits",
    "sample_rate": 22050,
    "language": "bn-Bangladesh",
    "batch_size": 16,
    "epochs": 1000
}
```

### **Step 3: Execute Training**
1. **Upload Script**: Add `kaggle_tts_training.py` to a Kaggle notebook
2. **Link Data**: Ensure all required datasets are connected
3. **Run Training**: Execute the script and monitor progress
4. **Save Results**: Use "Save & Run All" to preserve outputs

### **Step 4: Monitor Progress**
```python
# Script provides real-time feedback
✓ CUDA available - Device count: 2
✓ Found: /kaggle/input/datahrbnn/MyTTSDataset/train_tts.py
🚀 Launching TTS training...
✅ Training completed successfully!
```

---

## 📈 **Expected Outputs**

### **Training Artifacts**
- `checkpoint_*.pth`: Model checkpoints at regular intervals
- `config.json`: Final training configuration
- `train_log.txt`: Detailed training logs
- `validation_samples/`: Generated audio samples

### **Performance Metrics**
- **Training Loss**: Convergence over epochs
- **Validation Loss**: Generalization performance
- **Audio Quality**: Sample outputs for evaluation
- **Training Time**: Duration and resource utilization

---

## 🔍 **Troubleshooting**

### **Common Issues**

**Dataset Not Found**
```python
✗ Missing: /kaggle/input/datahrbnn/MyTTSDataset/train_tts.py
```
**Solution**: Verify dataset is properly linked in Kaggle interface

**GPU Not Available**
```python
⚠ CUDA not available - using CPU
```
**Solution**: Ensure GPU accelerator is enabled in notebook settings

**Training Timeout**
```python
⚠ Training timeout (6 hours) - process terminated
```
**Solution**: Reduce epochs or batch size for faster convergence

### **Memory Management**
- **Batch Size**: Reduce if encountering OOM errors
- **Model Size**: Use smaller architectures for limited GPU memory
- **Data Loading**: Implement efficient data loaders

---

## 🌟 **Advantages of Kaggle Training**

### **Resource Access**
- ✅ **Free GPU Hours**: ~30 GPU hours per week
- ✅ **High Memory**: 30GB RAM + 15GB GPU memory
- ✅ **Fast Storage**: SSD-based temporary and persistent storage

### **Collaboration**
- ✅ **Public Notebooks**: Share training experiments
- ✅ **Dataset Sharing**: Collaborate on data preparation
- ✅ **Version Control**: Built-in experiment tracking

### **Integration**
- ✅ **Pre-installed Libraries**: Extensive ML/DL ecosystem
- ✅ **Docker Environment**: Consistent runtime environment
- ✅ **Output Management**: Automatic result preservation

---

## 🔗 **Related Resources**

- **Kaggle Python Docker**: [GitHub Repository](https://github.com/kaggle/docker-python)
- **Coqui TTS**: Text-to-Speech training framework
- **VITS Model**: Variational Inference with adversarial learning
- **Bengali TTS**: Language-specific considerations

---

## 📝 **Notes**

This script is specifically designed for the **Bangladeshi Bangla TTS fine-tuning project** and integrates with the preprocessing pipeline established in previous stages. The training approach leverages transfer learning from pre-trained models to achieve efficient fine-tuning within Kaggle's resource constraints.

**Environment Compatibility**: The script is optimized for Kaggle's specific directory structure and resource limitations, making it an ideal solution for cloud-based TTS model development.