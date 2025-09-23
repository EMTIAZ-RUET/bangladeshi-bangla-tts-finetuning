import os
import base64
import requests

# GCP Configuration
GCP_API_KEY = ""
VOICE_NAME = "bn-Bangladesh-Chirp3-HD-Puck"  # Specific Bengali voice requested

# Create output directory
output_dir = "output_audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Find the last processed audio file
last_audio_id = None
audio_files = [f for f in os.listdir(output_dir) if f.endswith('.wav') and f.startswith('audio')]
if audio_files:
    # Extract numbers from filenames and find max
    audio_numbers = [int(f.replace('audio', '').replace('.wav', '')) for f in audio_files]
    if audio_numbers:
        last_audio_id = f"audio{max(audio_numbers)}"
        print(f"Last processed: {last_audio_id}")

# Process metadata
is_found_last = last_audio_id is  None  # If no last_audio_id, start from beginning
with open("testMetaData.txt", 'r', encoding='utf-8') as file:
    for line in file:
        if not line.strip():
            continue

        parts = line.strip().split('|')

        if len(parts) != 3:
            print(f"Skipping malformed line: {line.strip()}")
            continue

        if len(parts) == 3:
            audio_id = parts[0].strip()

            # print(audio_id)

            # Skip until we find the last processed audio
            if not is_found_last:
                if audio_id == last_audio_id:
                    is_found_last = True
                continue

            text_to_convert = parts[2].strip()
            output_file = os.path.join(output_dir, f"{audio_id}.wav")

            # Prepare GCP TTS request
            url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={GCP_API_KEY}"

            payload = {
                "input": {"text": text_to_convert},
                "voice": {
                    "languageCode": "bn-Bangladesh",
                    "name": VOICE_NAME
                },
                "audioConfig": {
                    "audioEncoding": "LINEAR16",
                    "sampleRateHertz": 24000
                }
            }

            # Make request
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                # Decode and save audio content
                audio_content = response.json().get("audioContent")
                if audio_content:
                    with open(output_file, "wb") as audio_file:
                        audio_file.write(base64.b64decode(audio_content))
                    print(f"Created: {output_file}")
            else:
                print(f"Error: {audio_id} - {response.status_code} - {response.text}")