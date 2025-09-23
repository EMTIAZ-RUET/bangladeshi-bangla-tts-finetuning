"""
Audio Cleaning Script for TTS Training Dataset

This script performs comprehensive audio preprocessing and cleaning for TTS model training.
It handles audio length trimming, silence removal, noise filtering, and quality validation.

Features:
    - Trims long audio files (>20 seconds) into smaller segments
    - Removes leading and trailing silence
    - Filters out noisy or poor quality recordings
    - Validates audio quality for TTS training
    - Splits long utterances while maintaining text alignment
    - Normalizes volume levels and removes artifacts

Usage:
    1. Ensure your audio files are in a 'wavs' or 'audio' directory
    2. Have corresponding metadata file with text transcriptions
    3. Run the script to clean and validate all audio files
    4. Output will be cleaned audio files and updated metadata

Dependencies:
    pip install librosa soundfile numpy scipy
"""

import os
import librosa
import soundfile as sf
import numpy as np
from scipy import signal
import re
import shutil
from pathlib import Path

class AudioCleaner:
    def __init__(self, target_sr=24000, max_duration=20.0, min_duration=1.0):
        """
        Initialize AudioCleaner with processing parameters.
        
        Args:
            target_sr: Target sample rate (24kHz for TTS)
            max_duration: Maximum duration in seconds (20s for stability)
            min_duration: Minimum duration in seconds (1s minimum)
        """
        self.target_sr = target_sr
        self.max_duration = max_duration
        self.min_duration = min_duration
        
        # Audio quality thresholds
        self.min_rms_threshold = 0.001  # Minimum RMS energy (avoid too quiet)
        self.max_rms_threshold = 0.9    # Maximum RMS energy (avoid clipping)
        self.silence_threshold = 0.01   # Threshold for silence detection
        self.min_speech_ratio = 0.3     # Minimum speech-to-total ratio
        
    def detect_silence(self, audio, threshold=None):
        """Detect silence segments in audio."""
        if threshold is None:
            threshold = self.silence_threshold
            
        # Calculate frame-wise energy
        frame_length = int(self.target_sr * 0.025)  # 25ms frames
        hop_length = int(frame_length // 4)
        
        energy = librosa.feature.rms(y=audio, frame_length=frame_length, 
                                   hop_length=hop_length)[0]
        
        # Find silence frames
        silence_frames = energy < threshold
        
        return silence_frames, energy
    
    def trim_silence(self, audio):
        """Remove leading and trailing silence from audio."""
        # Use librosa's trim function with custom parameters
        audio_trimmed, _ = librosa.effects.trim(
            audio, 
            top_db=30,  # Threshold in dB below peak
            frame_length=2048,
            hop_length=512
        )
        
        return audio_trimmed
    
    def validate_audio_quality(self, audio):
        """Validate if audio meets quality requirements for TTS."""
        issues = []
        
        # Check duration
        duration = len(audio) / self.target_sr
        if duration < self.min_duration:
            issues.append(f"Too short: {duration:.2f}s")
        elif duration > self.max_duration:
            issues.append(f"Too long: {duration:.2f}s")
        
        # Check RMS energy levels
        rms = np.sqrt(np.mean(audio ** 2))
        if rms < self.min_rms_threshold:
            issues.append(f"Too quiet: RMS={rms:.4f}")
        elif rms > self.max_rms_threshold:
            issues.append(f"Too loud/clipped: RMS={rms:.4f}")
        
        # Check for clipping
        clipping_ratio = np.sum(np.abs(audio) > 0.95) / len(audio)
        if clipping_ratio > 0.001:  # More than 0.1% clipped samples
            issues.append(f"Clipping detected: {clipping_ratio*100:.2f}%")
        
        # Check speech content ratio
        silence_frames, energy = self.detect_silence(audio)
        speech_ratio = 1.0 - (np.sum(silence_frames) / len(silence_frames))
        if speech_ratio < self.min_speech_ratio:
            issues.append(f"Too much silence: {speech_ratio*100:.1f}% speech")
        
        # Check for DC offset
        dc_offset = np.mean(audio)
        if abs(dc_offset) > 0.01:
            issues.append(f"DC offset: {dc_offset:.3f}")
        
        return len(issues) == 0, issues
    
    def normalize_audio(self, audio):
        """Normalize audio for consistent levels."""
        # Remove DC offset
        audio = audio - np.mean(audio)
        
        # Normalize to peak level of 0.95 (leaving headroom)
        peak = np.max(np.abs(audio))
        if peak > 0:
            audio = audio * (0.95 / peak)
        
        return audio
    
    def split_long_audio(self, audio, text, max_chars_per_second=15):
        """Split long audio into smaller segments based on text length."""
        duration = len(audio) / self.target_sr
        
        if duration <= self.max_duration:
            return [(audio, text)]
        
        # Estimate characters per second
        chars_per_second = len(text) / duration
        
        # Calculate optimal split points
        target_duration = self.max_duration * 0.8  # Target 80% of max for safety
        target_chars = int(target_duration * chars_per_second)
        
        segments = []
        
        # Split text at sentence boundaries
        sentences = re.split(r'([।?!.])', text)
        
        current_text = ""
        current_start = 0
        
        for i in range(0, len(sentences) - 1, 2):  # Step by 2 to include punctuation
            sentence = sentences[i] + (sentences[i+1] if i+1 < len(sentences) else "")
            
            if len(current_text + sentence) > target_chars and current_text:
                # Calculate audio segment
                char_ratio = len(current_text) / len(text)
                segment_end = int(char_ratio * len(audio))
                
                audio_segment = audio[current_start:segment_end]
                
                if len(audio_segment) > 0:
                    segments.append((audio_segment, current_text.strip()))
                
                current_text = sentence
                current_start = segment_end
            else:
                current_text += sentence
        
        # Add remaining segment
        if current_text:
            audio_segment = audio[current_start:]
            if len(audio_segment) > 0:
                segments.append((audio_segment, current_text.strip()))
        
        return segments
    
    def reduce_noise(self, audio):
        """Apply basic noise reduction using spectral subtraction."""
        # Simple noise reduction using median filtering
        # This is a basic implementation - more sophisticated methods could be used
        
        # Apply a small amount of noise reduction
        filtered_audio = signal.medfilt(audio, kernel_size=3)
        
        # Blend with original to avoid over-processing
        audio_cleaned = 0.8 * audio + 0.2 * filtered_audio
        
        return audio_cleaned
    
    def process_audio_file(self, audio_path, text=""):
        """Process a single audio file through the cleaning pipeline."""
        try:
            # Load audio
            audio, sr = librosa.load(audio_path, sr=self.target_sr, mono=True)
            
            # Step 1: Initial quality check
            is_valid, issues = self.validate_audio_quality(audio)
            
            if not is_valid and "Too short" in str(issues):
                return None, f"Skipped: {', '.join(issues)}"
            
            # Step 2: Trim silence
            audio = self.trim_silence(audio)
            
            # Step 3: Normalize audio
            audio = self.normalize_audio(audio)
            
            # Step 4: Basic noise reduction
            audio = self.reduce_noise(audio)
            
            # Step 5: Split if too long
            segments = self.split_long_audio(audio, text) if text else [(audio, "")]
            
            # Step 6: Final validation of segments
            valid_segments = []
            for segment_audio, segment_text in segments:
                is_valid, issues = self.validate_audio_quality(segment_audio)
                if is_valid:
                    valid_segments.append((segment_audio, segment_text))
                else:
                    print(f"  Warning: Segment rejected - {', '.join(issues)}")
            
            if not valid_segments:
                return None, "No valid segments after processing"
            
            return valid_segments, "Success"
            
        except Exception as e:
            return None, f"Error: {str(e)}"

def process_dataset(audio_dir, metadata_file, output_dir, output_metadata):
    """Process entire dataset of audio files."""
    cleaner = AudioCleaner()
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Statistics
    total_files = 0
    processed_files = 0
    skipped_files = 0
    segments_created = 0
    
    # Read metadata
    audio_text_map = {}
    if os.path.exists(metadata_file):
        with open(metadata_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        audio_id = parts[0]
                        text = parts[2]  # Use normalized text
                        audio_text_map[audio_id] = text
    
    print(f"Found {len(audio_text_map)} entries in metadata")
    
    # Process audio files
    with open(output_metadata, 'w', encoding='utf-8') as out_meta:
        for filename in os.listdir(audio_dir):
            if not filename.endswith('.wav'):
                continue
            
            total_files += 1
            audio_id = os.path.splitext(filename)[0]
            audio_path = os.path.join(audio_dir, filename)
            
            # Get corresponding text
            text = audio_text_map.get(audio_id, "")
            
            print(f"Processing {filename}...")
            
            # Process audio
            result, message = cleaner.process_audio_file(audio_path, text)
            
            if result is None:
                print(f"  Skipped: {message}")
                skipped_files += 1
                continue
            
            # Save processed segments
            for i, (segment_audio, segment_text) in enumerate(result):
                if len(result) == 1:
                    # Single segment - keep original filename
                    output_filename = filename
                    output_audio_id = audio_id
                else:
                    # Multiple segments - add suffix
                    base_name = os.path.splitext(filename)[0]
                    output_filename = f"{base_name}_{i+1}.wav"
                    output_audio_id = f"{audio_id}_{i+1}"
                
                output_path = os.path.join(output_dir, output_filename)
                
                # Save audio
                sf.write(output_path, segment_audio, cleaner.target_sr)
                
                # Write metadata entry
                original_text = segment_text if segment_text else text
                out_meta.write(f"{output_audio_id}|{original_text}|{segment_text or text}\\n")
                
                segments_created += 1
            
            processed_files += 1
            
            if total_files % 50 == 0:
                print(f"Progress: {total_files} files checked, {processed_files} processed")
    
    # Print summary
    print(f"\\n=== Audio Cleaning Summary ===")
    print(f"Total files found: {total_files}")
    print(f"Successfully processed: {processed_files}")
    print(f"Skipped files: {skipped_files}")
    print(f"Output segments created: {segments_created}")
    print(f"Cleaned audio saved to: {output_dir}")
    print(f"Updated metadata saved to: {output_metadata}")

def main():
    """Main function to run audio cleaning."""
    # Look for common audio directory names
    audio_dirs = ['wavs', 'audio', 'wav_files', 'sounds']
    audio_dir = None
    
    for dirname in audio_dirs:
        if os.path.exists(dirname) and os.path.isdir(dirname):
            audio_dir = dirname
            break
    
    if not audio_dir:
        print("Error: No audio directory found! Expected one of: wavs, audio, wav_files, sounds")
        print("Please create one of these directories and place your .wav files there.")
        return
    
    # Look for metadata files
    metadata_files = ['metadata.txt', 'metadata1.txt', 'metadata_normalized.txt']
    metadata_file = None
    
    for metafile in metadata_files:
        if os.path.exists(metafile):
            metadata_file = metafile
            break
    
    if not metadata_file:
        print("Warning: No metadata file found. Processing audio without text alignment.")
        metadata_file = "dummy_metadata.txt"
        # Create empty metadata file
        with open(metadata_file, 'w') as f:
            pass
    
    # Set output paths
    output_dir = "cleaned_audio"
    output_metadata = "cleaned_metadata.txt"
    
    print(f"=== Audio Cleaning Configuration ===")
    print(f"Input audio directory: {audio_dir}")
    print(f"Input metadata file: {metadata_file}")
    print(f"Output audio directory: {output_dir}")
    print(f"Output metadata file: {output_metadata}")
    print(f"Target sample rate: 24000 Hz")
    print(f"Max audio duration: 20.0 seconds")
    print(f"Min audio duration: 1.0 seconds")
    print("="*40)
    
    # Count files to process
    wav_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]
    print(f"Found {len(wav_files)} .wav files to process\\n")
    
    if len(wav_files) == 0:
        print("No .wav files found in the audio directory!")
        return
    
    # Start processing
    process_dataset(audio_dir, metadata_file, output_dir, output_metadata)

if __name__ == "__main__":
    main()