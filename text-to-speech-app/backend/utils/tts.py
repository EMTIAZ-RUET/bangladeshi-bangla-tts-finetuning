import re
import os
import torch
import bangla
from bnnumerizer import numerize
from bnunicodenormalizer import Normalizer
from huggingface_hub import snapshot_download
from TTS.api import TTS as CoquiTTS

from .modules.synthsizer import Synthesizer
from .logger_config import app_logger as logger
from .config import MODEL_DIRECTORY

class TTS:
    def __init__(self):
        # Available models configuration
        self.available_models = {
            "finetuned": {
                "name": "Fine-tuned Model (Your Custom Model)",
                "folder": "vits-female-finetuned-quantized",
                "repo_id": None,  # Local model
                "description": "Your custom fine-tuned VITS model",
                "type": "local"
            },
            "pretrained": {
                "name": "Pre-trained Model (Coqui VITS)",
                "model_name": "tts_models/bn/custom/vits-female",
                "repo_id": None,  # Coqui TTS model
                "description": "Pre-trained Bangla VITS model from Coqui TTS",
                "type": "coqui"
            }
        }
        
        # Load both models
        self.models = {}
        self._load_all_models()
    
    def _load_all_models(self):
        """Load all available models."""
        for model_key, model_info in self.available_models.items():
            try:
                logger.info(f"Loading {model_info['name']}...")
                
                if model_info['type'] == 'local':
                    # Load local fine-tuned model
                    model_path, config_path = self._get_model_paths(model_key)
                    model = self.model_synthesizer(model_path, config_path)
                    self.models[model_key] = model
                elif model_info['type'] == 'coqui':
                    # Load Coqui TTS model
                    model = CoquiTTS(model_name=model_info['model_name'])
                    self.models[model_key] = model
                
                logger.info(f"✅ Successfully loaded {model_info['name']}")
            except Exception as e:
                logger.warning(f"❌ Failed to load {model_info['name']}: {e}")
                self.models[model_key] = None

    def normalize(self, sen):
        bnorm=Normalizer()
        _words = [bnorm(word)['normalized']  for word in sen.split()]
        return " ".join([word for word in _words if word is not None])
    
    def model_synthesizer(self, model_path="models/pytorch_model.pth", config_path="models/config.json"):
        model =Synthesizer(
            model_path,
            config_path,
            use_cuda = True if torch.cuda.is_available() else False,
        )
        return model

    def get_available_models(self):
        """Get list of available models with their status."""
        models_info = {}
        for model_key, model_info in self.available_models.items():
            models_info[model_key] = {
                "name": model_info["name"],
                "description": model_info["description"],
                "loaded": self.models.get(model_key) is not None
            }
        return models_info
    
    def bangla_tts(self, text="আমি বাংলা টেক্সট টু স্পিচ ব্যবহার করছি।", model_type="finetuned", is_male=True, is_e2e_vits=True, log_dir="logs/unknown.wav"):
        '''
        params:
            text : input bangla text that needs to be synthesized.
            model_type : "finetuned" or "pretrained" - which model to use
            is_male : if True then uses cloned voice of male speaker,otherwise female speaker is used.
            is_e2e_vits : if True then uses vits model,otherwise glowtts gets used.
        '''
        # Check if the requested model is available
        if model_type not in self.models or self.models[model_type] is None:
            available_models = [k for k, v in self.models.items() if v is not None]
            raise ValueError(f"Model '{model_type}' not available. Available models: {available_models}")
        
        selected_model = self.models[model_type]
        model_info = self.available_models[model_type]
        logger.info(f"Using {model_info['name']} for TTS")
        
        # Text preprocessing
        if(text[-1] != '।'):
            text += '।'
        # english numbers to bangla conversion
        res = re.search('[0-9]', text)
        if res is not None:
            text = bangla.convert_english_digit_to_bangla_digit(text)
        
        #replace ':' in between two bangla numbers with ' এর '
        pattern=r"[০, ১, ২, ৩, ৪, ৫, ৬, ৭, ৮, ৯]:[০, ১, ২, ৩, ৪, ৫, ৬, ৭, ৮, ৯]"
        matches=re.findall(pattern,text)
        for m in matches:
            r=m.replace(":"," এর ")
            text=text.replace(m,r)
        try:
            text=numerize(text)
        except:
            pass
        text = self.normalize(text)
        
        # Generate audio based on model type
        if model_info['type'] == 'local':
            # Use local fine-tuned model
            sentenceEnders = re.compile('[।!?]')
            sentences = sentenceEnders.split(str(text))
            audio_list = []
            for i in range(len(sentences)):
                if(not sentences[i]):
                    continue
                sentence_text = sentences[i]+'।'
                audio_list.append(torch.as_tensor(selected_model.tts(sentence_text)))
            audio = torch.cat([k for k in audio_list])
            numpy_audio = audio.detach().cpu().numpy()
        elif model_info['type'] == 'coqui':
            # Use Coqui TTS model
            numpy_audio = selected_model.tts(text)
        
        return numpy_audio
    
    def _get_model_paths(self, model_key):
        """Get model and config paths for local models only."""
        model_info = self.available_models[model_key]
        
        if model_info['type'] != 'local':
            raise ValueError(f"_get_model_paths only works with local models, got {model_info['type']}")
            
        local_dir = os.path.join(MODEL_DIRECTORY, model_info["folder"])
        model_path = os.path.join(local_dir, "pytorch_model.pth")
        
        # Check for different possible config file names
        possible_config_names = ["config.json", "config_100 epoch.json", "config_100epoch.json"]
        config_path = None
        
        for config_name in possible_config_names:
            potential_config_path = os.path.join(local_dir, config_name)
            if os.path.exists(potential_config_path):
                config_path = potential_config_path
                break
        
        # Verify both files exist
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        if not config_path:
            raise FileNotFoundError(f"Config file not found. Looked for: {possible_config_names} in {local_dir}")
        
        logger.info(f"Using local model files from: {local_dir}")
        logger.info(f"Model: {model_path}")
        logger.info(f"Config: {config_path}")
        
        return model_path, config_path
    
