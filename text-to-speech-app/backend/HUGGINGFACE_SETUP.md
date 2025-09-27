# Hugging Face Model Upload Guide

This guide will help you upload your custom fine-tuned Bangladeshi Bangla TTS model to Hugging Face Hub.

## Prerequisites

1. **Hugging Face Account**: Create an account at [huggingface.co](https://huggingface.co)
2. **Access Token**: Generate a write access token from your Hugging Face settings

## Step 1: Install Required Dependencies

Update your requirements.txt to include Hugging Face Hub:

```bash
pip install huggingface-hub
```

## Step 2: Authentication

### Option A: Login via CLI (Recommended)
```bash
huggingface-cli login
```
Enter your access token when prompted.

### Option B: Set Environment Variable
```bash
export HUGGINGFACE_HUB_TOKEN="your_token_here"
```

### Option C: Pass Token Directly
You can pass the token directly to the upload script (less secure).

## Step 3: Get Your Access Token

1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Choose "Write" permissions
4. Copy the generated token

## Step 4: Upload Your Model

Run the upload script with your details:

```bash
cd /home/bs00728/bangladeshi-bangla-tts-finetuning/text-to-speech-app/backend

python huggingface_upload.py \
    --model-name "bangladeshi-bangla-tts-vits" \
    --username "your-huggingface-username"
```

### With Token (if not logged in via CLI):
```bash
python huggingface_upload.py \
    --model-name "bangladeshi-bangla-tts-vits" \
    --username "your-huggingface-username" \
    --token "your_access_token"
```

## Step 5: Update Your Code

After uploading, update the repo_id in your TTS class:

1. Open `utils/tts.py`
2. Find the `huggingface` model configuration
3. Replace `"your-username/bangladeshi-bangla-tts-vits"` with your actual repo ID

Example:
```python
"huggingface": {
    "name": "Hugging Face Model (Your Custom Model)",
    "repo_id": "emtiaz-ruet/bangladeshi-bangla-tts-vits",  # Your actual repo
    "description": "Your custom fine-tuned VITS model from Hugging Face",
    "type": "huggingface"
},
```

## Step 6: Test Your Model

Test loading from Hugging Face:

```python
from utils import TTS

# Initialize TTS with Hugging Face model
tts = TTS()

# Use the Hugging Face model
audio = tts.bangla_tts(
    text="আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি।",
    model_type="huggingface"
)
```

## Step 7: Update Your API

Your FastAPI application will now support three model types:
- `"finetuned"` - Local model
- `"huggingface"` - Model from Hugging Face Hub
- `"pretrained"` - Coqui TTS model

Example API request:
```json
{
    "text": "আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি।",
    "session_id": "your-session-id",
    "model_type": "huggingface"
}
```

## Troubleshooting

### Common Issues:

1. **Authentication Error**:
   - Make sure you're logged in: `huggingface-cli whoami`
   - Check your token has write permissions

2. **Model Not Found**:
   - Verify the repo_id is correct
   - Make sure the repository is public or you have access

3. **File Not Found**:
   - Ensure `pytorch_model.pth` and `config_finetuned.json` exist in your models directory

4. **Upload Timeout**:
   - Large models (997MB) may take time to upload
   - Check your internet connection

### Getting Help:

- Check the upload logs for detailed error messages
- Visit [Hugging Face Documentation](https://huggingface.co/docs/hub/index)
- Open an issue in your repository

## Model Repository Structure

After upload, your Hugging Face repository will contain:

```
your-username/bangladeshi-bangla-tts-vits/
├── README.md                 # Model card with documentation
├── config.json              # Model configuration
├── pytorch_model.pth        # Your trained model weights
├── requirements.txt         # Dependencies
└── model_info.json         # Additional metadata
```

## Sharing Your Model

Once uploaded, your model will be available at:
`https://huggingface.co/your-username/bangladeshi-bangla-tts-vits`

Others can use your model with:
```python
from huggingface_hub import snapshot_download

# Download your model
model_path = snapshot_download(repo_id="your-username/bangladeshi-bangla-tts-vits")
```

## Next Steps

1. **Test thoroughly**: Ensure the Hugging Face model works as expected
2. **Update documentation**: Add usage examples to your repository
3. **Share with community**: Announce your model on social media or forums
4. **Collect feedback**: Monitor issues and improve based on user feedback

## Security Notes

- Never commit access tokens to version control
- Use environment variables or CLI login for authentication
- Consider making your repository private if it contains sensitive data
- Regularly rotate your access tokens
