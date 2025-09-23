import os
import torchaudio
import torch
import numpy as np

# Path to wavs folder
wavs_folder = "wavs"

# Target sample rate
sample_rate = 22050

# Process all wav files in the folder
for filename in os.listdir(wavs_folder):
    if filename.endswith(".wav"):
        file_path = os.path.join(wavs_folder, filename)

        # Load the audio file
        waveform, orig_sample_rate = torchaudio.load(file_path)

        # Resample if needed
        if orig_sample_rate != sample_rate:
            resampler = torchaudio.transforms.Resample(
                orig_freq=orig_sample_rate,
                new_freq=sample_rate
            )
            waveform = resampler(waveform)

        # Normalize audio to range [-0.95, 0.95] to ensure it's safely within [-1, 1]
        # First check if normalization is needed
        max_val = torch.max(torch.abs(waveform))

        if max_val > 0.95:
            # Normalize to peak of 0.95 to leave some headroom
            waveform = waveform * (0.95 / max_val)

        # Save back to the same file
        torchaudio.save(file_path, waveform, sample_rate)

        print(f"Processed {filename}: resampled to {sample_rate}Hz and normalized to range [-0.95, 0.95]")

print("All audio files processed successfully!")