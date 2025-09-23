"""
Bangla Text Normalization Script for TTS Training Dataset

This script performs text normalization on Bangla text data to prepare it for TTS model training.
It handles numerical conversion and Unicode standardization while preserving all punctuation.

Features:
    - Converts numbers to spoken Bangla form
    - Normalizes Unicode variations of Bangla characters
    - Preserves all original punctuation marks
    - Normalizes whitespace only
    - Validates text for TTS training compatibility

Usage:
    1. Ensure your metadata file (metadata.txt or metadata1.txt) is in the same directory
    2. Run the script to normalize all text entries
    3. Output will be saved to a new normalized metadata file

Input Format: audio_id|original_text|normalized_text
Output Format: audio_id|original_text|normalized_text_with_numbers_converted
"""

import re
import unicodedata
import os

class BanglaTextNormalizer:
    def __init__(self):
        # Bangla number mappings
        self.bangla_numbers = {
            '0': 'শূন্য', '1': 'এক', '2': 'দুই', '3': 'তিন', '4': 'চার',
            '5': 'পাঁচ', '6': 'ছয়', '7': 'সাত', '8': 'আট', '9': 'নয়'
        }
        
        # English number words to Bangla
        self.english_to_bangla_numbers = {
            'zero': 'শূন্য', 'one': 'এক', 'two': 'দুই', 'three': 'তিন', 'four': 'চার',
            'five': 'পাঁচ', 'six': 'ছয়', 'seven': 'সাত', 'eight': 'আট', 'nine': 'নয়',
            'ten': 'দশ', 'eleven': 'এগারো', 'twelve': 'বারো', 'thirteen': 'তেরো',
            'fourteen': 'চৌদ্দ', 'fifteen': 'পনেরো', 'sixteen': 'ষোলো',
            'seventeen': 'সতেরো', 'eighteen': 'আঠারো', 'nineteen': 'উনিশ',
            'twenty': 'বিশ', 'thirty': 'ত্রিশ', 'forty': 'চল্লিশ', 'fifty': 'পঞ্চাশ',
            'sixty': 'ষাট', 'seventy': 'সত্তর', 'eighty': 'আশি', 'ninety': 'নব্বই',
            'hundred': 'শত', 'thousand': 'হাজার', 'million': 'লক্ষ'
        }
        
        
    def normalize_numbers(self, text):
        """Convert numeric digits and English number words to Bangla spoken form."""
        # Convert individual digits
        for digit, bangla in self.bangla_numbers.items():
            text = text.replace(digit, bangla)
        
        # Convert English number words to Bangla
        for eng_num, bangla_num in self.english_to_bangla_numbers.items():
            # Case-insensitive replacement
            text = re.sub(r'\b' + eng_num + r'\b', bangla_num, text, flags=re.IGNORECASE)
        
        return text
    
    def normalize_whitespace(self, text):
        """Normalize whitespace without affecting punctuation."""
        # Only clean up extra whitespace
        text = re.sub(r'\s+', ' ', text)  # Multiple spaces to single space
        return text.strip()
    
    def normalize_unicode(self, text):
        """Normalize Unicode variations of Bangla characters."""
        # Normalize to NFC (Canonical Decomposition followed by Canonical Composition)
        text = unicodedata.normalize('NFC', text)
        
        # Handle common Unicode variations
        replacements = {
            '\u09b7': 'ষ',  # Normalize various forms of ষ
            '\u09a4\u09cd\u09a4': 'ত্ত',  # ত্ত normalization
            '\u09a8\u09cd\u09a8': 'ন্ন',  # ন্ন normalization
            '\u09b2\u09cd\u09b2': 'ল্ল',  # ল্ল normalization
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text
    
    def preserve_original_format(self, text):
        """Preserve original text format without removing any characters."""
        # Only clean up extra whitespace
        return re.sub(r'\s+', ' ', text).strip()
    
    def validate_text(self, text):
        """Validate if text is suitable for TTS training."""
        # Check if text is not empty
        if not text or not text.strip():
            return False, "Empty text"
        
        # Check minimum length (at least 3 words)
        words = text.strip().split()
        if len(words) < 3:
            return False, f"Too short ({len(words)} words)"
        
        # Check maximum length (not more than 50 words for TTS)
        if len(words) > 50:
            return False, f"Too long ({len(words)} words)"
        
        # Check for proper sentence ending
        if not text.strip().endswith(('।', '?', '!', '.')):
            return False, "No proper sentence ending"
        
        return True, "Valid"
    
    def normalize_text(self, text):
        """Apply normalization steps to the text while preserving punctuation."""
        if not text:
            return ""
        
        # Step 1: Normalize Unicode
        text = self.normalize_unicode(text)
        
        # Step 2: Convert numbers to spoken form
        text = self.normalize_numbers(text)
        
        # Step 3: Normalize whitespace only (preserve all punctuation)
        text = self.normalize_whitespace(text)
        
        return text

def process_metadata_file(input_file, output_file):
    """Process metadata file and normalize all text entries."""
    normalizer = BanglaTextNormalizer()
    
    processed_count = 0
    error_count = 0
    validation_errors = []
    
    print(f"Processing {input_file}...")
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split('|')
                if len(parts) != 3:
                    print(f"Warning: Malformed line {line_num}: {line}")
                    error_count += 1
                    continue
                
                audio_id, original_text, old_normalized_text = parts
                
                # Normalize the text
                new_normalized_text = normalizer.normalize_text(old_normalized_text)
                
                # Validate the normalized text
                is_valid, validation_msg = normalizer.validate_text(new_normalized_text)
                
                if not is_valid:
                    validation_errors.append(f"{audio_id}: {validation_msg}")
                    # Still include it but mark as potentially problematic
                    print(f"Warning: {audio_id} - {validation_msg}")
                
                # Write to output file
                outfile.write(f"{audio_id}|{original_text}|{new_normalized_text}\\n")
                processed_count += 1
                
                if processed_count % 100 == 0:
                    print(f"Processed {processed_count} entries...")
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found!")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False
    
    # Print summary
    print(f"\\n=== Text Normalization Summary ===")
    print(f"Total entries processed: {processed_count}")
    print(f"Malformed lines skipped: {error_count}")
    print(f"Validation warnings: {len(validation_errors)}")
    print(f"Output saved to: {output_file}")
    
    if validation_errors and len(validation_errors) <= 10:
        print(f"\\nValidation warnings:")
        for error in validation_errors:
            print(f"  - {error}")
    elif len(validation_errors) > 10:
        print(f"\\nFirst 10 validation warnings:")
        for error in validation_errors[:10]:
            print(f"  - {error}")
        print(f"  ... and {len(validation_errors) - 10} more")
    
    return True

def main():
    """Main function to run text normalization."""
    # Check for input files
    input_files = ['metadata.txt', 'metadata1.txt']
    found_files = [f for f in input_files if os.path.exists(f)]
    
    if not found_files:
        print("Error: No metadata files found! Expected 'metadata.txt' or 'metadata1.txt'")
        return
    
    for input_file in found_files:
        # Create output filename
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_normalized.txt"
        
        print(f"\\n{'='*50}")
        print(f"Processing {input_file}")
        print(f"{'='*50}")
        
        success = process_metadata_file(input_file, output_file)
        
        if success:
            print(f"Successfully normalized text data from {input_file}")
        else:
            print(f"Failed to process {input_file}")

if __name__ == "__main__":
    main()