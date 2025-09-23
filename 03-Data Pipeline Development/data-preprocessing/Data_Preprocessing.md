# Data Preprocessing

To ensure the dataset was consistent, clean, and ready for fine-tuning, I applied a series of **text and audio preprocessing steps**. These transformations were designed to maintain **linguistic integrity**, standardize **acoustic properties**, and align with the **LJSpeech data format**, which is widely used for TTS model training.

---

## 1. Audio Preprocessing

* **Sampling Rate Adjustment**

  * All audio files were resampled to **24 kHz**, which strikes a balance between **speech quality** and **GPU memory constraints**.
  * This ensured uniformity across both the OpenSLR Bangla recordings and the Google TTS Zephyr synthetic audio.

* **Audio Length Trimming**

  * Long utterances (> 20 seconds) were cut into **smaller segments** to reduce training instability.
  * This also improved **alignment between text and audio**, minimizing issues like **attention collapse** during fine-tuning.

* **Silence & Noise Handling**

  * Leading and trailing silences were trimmed.
  * Noisy recordings were filtered out to ensure the dataset primarily contained **clear, intelligible speech**.

---

## 2. Text Normalization

* **Numerical Normalization**

  * Converted numbers into spoken form (e.g., "123" → "one hundred twenty-three").
  * Prevented the model from mispronouncing digits or learning inconsistent numeral readings.

* **Punctuation Cleanup**

  * Removed unwanted characters (extra symbols, emojis, foreign marks).
  * Standardized punctuation to **commas, periods, and question marks** for clarity in prosody.

* **Character & Token Normalization**

  * Standardized different Unicode variations of Bangla characters.
  * Normalized spacing and removed duplicated punctuation to make transcripts consistent.

---

## 3. Dataset Structuring (LJSpeech Format Conversion)

* Converted both **OpenSLR Bangla** and **Google TTS Zephyr** data into the **LJSpeech-style metadata.csv** format:

  ```
  file_path|raw_text|normalized_text
  ```

  * `file_path`: Relative path to the audio file.
  * `raw_text`: Original transcription.
  * `normalized_text`: Cleaned, standardized text after preprocessing.

* This structure allowed for **seamless integration with VITS pipelines**, which expect LJSpeech-style input.

---

## 4. Preprocessing Justification

* **Consistency**: By unifying sampling rate, text normalization, and format, the model could learn more effectively.
* **Robustness**: Removing noise and trimming audio reduced misalignments and improved training stability.
* **Adaptability**: LJSpeech-style format made it easier to adapt existing TTS architectures without rewriting input pipelines.
* **Linguistic Clarity**: Normalization ensured numerals, punctuation, and Bangla orthography were standardized, preventing **unintended speech artifacts**.