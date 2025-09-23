"""
Bangla Text Data Generation Script for TTS Training Dataset

This script uses Google Gemini API to generate conversational Bangla sentences
for training a Text-to-Speech model. It creates metadata.txt file with original
and normalized text pairs.

Usage:
    1. Ensure 'chunks_bangla.txt' file exists in the same directory
    2. Set your Gemini API key in the api_key variable
    3. Run the script to generate training data

Output:
    - metadata1.txt: Contains audio_id|original_text|normalized_text format
"""

import requests
import os
import re

# Read the text file
with open("chunks_bangla.txt", "r", encoding="utf-8") as file:
    text_content = file.read()

# Set up API request - Replace with your actual API key
api_key = "*************************************"
# Check if API key is set
if api_key == "*************************************":
    print("Error: Please set your actual Gemini API key in the 'api_key' variable.")
    exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

# Prompt for generating Bangla sentences with specific linguistic requirements
prompt = f"""
I need to create 200 conversational Bangla sentences for a Text-to-Speech training dataset based on this text content:

{text_content}

For each, output in the following format:
text: [original Bangla sentence]
normalized text: [normalized version of that sentence where numbers and acronyms are spelled out in Bangla]

Rules:
1. Each Bangla sentence must be at least 10–20 words long and related to the content.
2. Include these Bangla cluster words 3–5 times each:
   ক্রমশ, ক্লেস, খ্রিস্টান, খেলেফিক্স, গ্লানি, গ্রহণ, ঘ্রাণ, ট্রাপিক, ড্রাগন, ত্রাস, থ্রোন, দুর্বণ, ধ্রুবক, প্রভাব, প্লাবন, ফ্রেম, ফ্লোর, ব্রত, ব্লগার, ভ্রমণ, ম্রিয়মাণ, ম্লান, শ্রমিক, শ্রদ্ধা, স্লোগান, স্ট্রোক, স্টেশন, স্পন্দন, স্ক্রিপ্ট, স্ক্লেরা, স্কুল, স্বপ্ন, স্ট্রীরোগ, স্তবক, স্থাপত্য, স্নান, সফটিক, স্মৃতি, স্প্রিন্টার
3. Frequently use these common Bangla words:
   ও, করে, না, এই, এবং, করা, থেকে, হবে, একটি, এর, এ, জন্য, হয়, তিনি, তার, কিন্তু, আর, কী, যা, যে
4. Use ONLY Bangla in sentences.
5. End statements with Bangla dari (।) and questions with question marks (?)

Return in this format only:
text: sentence
normalized text: normalized_sentence

Repeat 200 times.
"""

payload = {
    "contents": [{
        "parts": [{"text": prompt}]
    }]
}

# Find the last audio number in the existing metadata.txt file
last_audio_num = 0  # Default starting value as shown in your example
if os.path.exists("metadata1.txt"):
    with open("metadata1.txt", "r", encoding="utf-8") as meta_file:
        for line in meta_file:
            if line.strip():
                match = re.match(r'audio(\d+)\|', line)
                if match:
                    audio_num = int(match.group(1))
                    last_audio_num = max(last_audio_num, audio_num)

print("Making API request to Gemini...")

# Make API request with error handling
try:
    response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)
    response.raise_for_status()  # Raise an exception for bad status codes
    result = response.json()
    
    # Extract the generated text
    if 'candidates' in result and len(result['candidates']) > 0:
        generated_text = result['candidates'][0]['content']['parts'][0]['text']
        print("Successfully received response from Gemini API")
    else:
        print("Error: No candidates found in API response")
        exit(1)
        
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
    exit(1)
except KeyError as e:
    print(f"Error parsing API response: {e}")
    exit(1)

print("Processing generated text and updating metadata...")

# Process the text to extract sentence pairs and write to metadata1.txt
sentences_added = 0
with open("metadata1.txt", "a", encoding="utf-8") as meta_file:
    lines = generated_text.strip().split('\n')
    i = 0
    current_audio_num = last_audio_num + 1

    while i < len(lines):
        line = lines[i].strip()

        # Skip any non-content lines (like code blocks or empty lines)
        if line.startswith('```') or line.endswith('```') or not line:
            i += 1
            continue

        # Check if the line starts with "text:"
        if line.startswith("text:"):
            original_text = line[5:].strip()  # Extract original text

            # Check if there's a normalized text line that follows
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("normalized text:"):
                normalized_text = lines[i + 1].strip()[15:].strip()  # Extract normalized text

                # Write to metadata1.txt in the required format: audio_id|original_text|normalized_text
                meta_file.write(f"audio{current_audio_num}|{original_text}|{normalized_text}\n")
                sentences_added += 1
                current_audio_num += 1
                i += 2  # Move past both lines
            else:
                # If the format is unexpected, use the original text for both fields
                meta_file.write(f"audio{current_audio_num}|{original_text}|{original_text}\n")
                sentences_added += 1
                current_audio_num += 1
                i += 1
        else:
            # Skip lines that don't match expected format
            i += 1

if sentences_added > 0:
    print(f"Successfully added {sentences_added} sentences to metadata1.txt")
    print(f"Audio IDs range: audio{last_audio_num + 1} to audio{current_audio_num - 1}")
else:
    print("Warning: No sentences were added to metadata1.txt")
