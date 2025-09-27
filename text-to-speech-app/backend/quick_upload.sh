#!/bin/bash

# Quick Upload Script for Bangladeshi Bangla TTS Model to Hugging Face
# Usage: ./quick_upload.sh your-username model-name

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Bangladeshi Bangla TTS Model Upload to Hugging Face${NC}"
echo "=================================================="

# Check if arguments are provided
if [ $# -lt 2 ]; then
    echo -e "${RED}❌ Error: Missing arguments${NC}"
    echo "Usage: $0 <huggingface-username> <model-name>"
    echo "Example: $0 emtiaz-ruet bangladeshi-bangla-tts-vits"
    exit 1
fi

USERNAME=$1
MODEL_NAME=$2

echo -e "${YELLOW}📋 Configuration:${NC}"
echo "  Username: $USERNAME"
echo "  Model Name: $MODEL_NAME"
echo "  Repository: $USERNAME/$MODEL_NAME"
echo ""

# Check if model files exist
echo -e "${BLUE}🔍 Checking model files...${NC}"
if [ ! -f "models/vits-female-finetuned-quantized/pytorch_model.pth" ]; then
    echo -e "${RED}❌ Model file not found: models/vits-female-finetuned-quantized/pytorch_model.pth${NC}"
    exit 1
fi

if [ ! -f "models/vits-female-finetuned-quantized/config_finetuned.json" ]; then
    echo -e "${RED}❌ Config file not found: models/vits-female-finetuned-quantized/config_finetuned.json${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Model files found${NC}"

# Check if huggingface-cli is installed and user is logged in
echo -e "${BLUE}🔐 Checking Hugging Face authentication...${NC}"
if ! command -v huggingface-cli &> /dev/null; then
    echo -e "${YELLOW}⚠️ huggingface-cli not found. Installing...${NC}"
    pip install huggingface-hub[cli]
fi

# Check if user is logged in
if ! huggingface-cli whoami &> /dev/null; then
    echo -e "${YELLOW}⚠️ Not logged in to Hugging Face. Please login:${NC}"
    echo "Run: huggingface-cli login"
    echo "Then run this script again."
    exit 1
fi

CURRENT_USER=$(huggingface-cli whoami)
echo -e "${GREEN}✅ Logged in as: $CURRENT_USER${NC}"

# Run the upload script
echo -e "${BLUE}🚀 Starting model upload...${NC}"
python huggingface_upload.py --model-name "$MODEL_NAME" --username "$USERNAME"

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}🎉 SUCCESS! Model uploaded successfully!${NC}"
    echo ""
    echo -e "${YELLOW}📍 Next Steps:${NC}"
    echo "1. Update your TTS class configuration:"
    echo "   - Open utils/tts.py"
    echo "   - Change repo_id to: \"$USERNAME/$MODEL_NAME\""
    echo ""
    echo "2. Test your model:"
    echo "   - Use model_type=\"huggingface\" in your API calls"
    echo ""
    echo "3. Visit your model:"
    echo "   - https://huggingface.co/$USERNAME/$MODEL_NAME"
    echo ""
else
    echo -e "${RED}❌ Upload failed! Check the error messages above.${NC}"
    exit 1
fi
