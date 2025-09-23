# import requests
# import csv
# import os
#
# # Read the text file
# with open("chunks_bangla.txt", "r", encoding="utf-8") as file:
#     text_content = file.read()
#
# # Set up API request
# api_key = "AIzaSyByNgUwGB5Iut5HPOqCaCEfGw76cBxeoE4"
# url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
#
# prompt = f"""
# I need to create 200 conversational Bangla sentences for a Text-to-Speech training dataset based on this text content:
#
# {text_content}
#
# Generate 200 natural Bangla sentences (at least 10-20 words each) that:
# 1. Maintain the context, themes, and vocabulary from the provided text content
# 2. Include each of these Bangla cluster words (with 3-5 repetitions for complex ones):
#    ক্রমশ, ক্লেস, খ্রিস্টান, খেলেফিক্স, গ্লানি, গ্রহণ, ঘ্রাণ, ট্রাপিক, ড্রাগন, ত্রাস, থ্রোন, দুর্বণ, ধ্রুবক, প্রভাব, প্লাবন, ফ্রেম, ফ্লোর, ব্রত, ব্লগার, ভ্রমণ, ম্রিয়মাণ, ম্লান, শ্রমিক, শ্রদ্ধা, স্লোগান, স্ট্রোক, স্টেশন, স্পন্দন, স্ক্রিপ্ট, স্ক্লেরা, স্কুল, স্বপ্ন, স্ট্রীরোগ, স্তবক, স্থাপত্য, স্নান, সফটিক, স্মৃতি, স্প্রিন্টার
#
# 3. Frequently use these common Bangla words:
#    ও, করে, না, এই, এবং, করা, থেকে, হবে, একটি, এর, এ, জন্য, হয়, তিনি, তার, কিন্তু, আর, কী, যা, যে
#
# 4. Ensure sentences are:
#    - Conversational and emotionally diverse
#    - Natural in structure and tone
#    - Related to the topics in the provided text content
#    - Contain ONLY Bangla words
#
# FORMAT:
# - For statements: End with Bangla dari (।)
# - For questions: End with question mark (?)
# - If including Bangla numerals, change the pronunciation in parentheses
#   Example: পঁচিশ, একশ
# - Return ONLY the Bangla sentences, one per line, with no additional text or explanations
# """
#
# payload = {
#     "contents": [{
#         "parts": [{"text": prompt}]
#     }]
# }
#
# # Make API request
# response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)
# result = response.json()
#
# # Extract the generated text
# generated_text = result['candidates'][0]['content']['parts'][0]['text']
#
# # Create incremental file name
# base_filename = "conversation_data"
# extension = ".csv"
# counter = 1
# output_filename = f"{base_filename}{extension}"
#
# while os.path.exists(output_filename):
#     output_filename = f"{base_filename}_{counter}{extension}"
#     counter += 1
#
# # Write to CSV with only one column
# with open(output_filename, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["text"])  # Only one column header
#
#     # Process each line and write to CSV
#     for line in generated_text.strip().split('\n'):
#         if line.strip() and not line.startswith('```') and not line.endswith('```'):
#             writer.writerow([line.strip()])  # Write only the text value
#
# print(f"CSV file '{output_filename}' generated successfully!")


import requests
import os
import re

# Read the text file
with open("chunks_bangla.txt", "r", encoding="utf-8") as file:
    text_content = file.read()

# Set up API request
api_key = "AIzaSyByNgUwGB5Iut5HPOqCaCEfGw76cBxeoE4"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

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

# Make API request
response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)
result = response.json()

# Extract the generated text
generated_text = result['candidates'][0]['content']['parts'][0]['text']

# Process the text to extract sentence pairs and write to metadata.txt
with open("metadata1.txt", "a", encoding="utf-8") as meta_file:
    lines = generated_text.strip().split('\n')
    i = 0
    current_audio_num = last_audio_num + 1

    while i < len(lines):
        line = lines[i].strip()

        # Skip any non-content lines (like code blocks)
        if line.startswith('```') or line.endswith('```') or not line:
            i += 1
            continue

        # Check if the line starts with "text:"
        if line.startswith("text:"):
            original_text = line[5:].strip()  # Extract original text

            # Check if there's a normalized text line that follows
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("normalized text:"):
                normalized_text = lines[i + 1].strip()[15:].strip()  # Extract normalized text

                # Write to metadata.txt in the required format
                meta_file.write(f"audio{current_audio_num}|{original_text}|{normalized_text}\n")
                current_audio_num += 1
                i += 2  # Move past both lines
            else:
                # If the format is unexpected, just use the original text for both
                meta_file.write(f"audio{current_audio_num}|{original_text}|{original_text}\n")
                current_audio_num += 1
                i += 1
        else:
            # If the line doesn't match expected format, skip it
            i += 1

print(f"Metadata updated successfully! Added sentences from audio{last_audio_num + 1} to audio{current_audio_num - 1}")