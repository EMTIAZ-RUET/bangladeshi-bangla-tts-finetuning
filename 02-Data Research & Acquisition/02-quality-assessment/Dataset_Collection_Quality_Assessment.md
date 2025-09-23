# Dataset Collection & Quality Assessment

For this fine-tuning task, a **hybrid dataset strategy** was adopted, combining **natural Bangladeshi Bangla speech and synthetic Bangladeshi TTS data**, with reference to **phonetic principles from the SUST (Shahjalal University of Science and Technology) TTS Corpus**. This ensures **linguistic diversity, accent consistency, phonetic coverage, and prosody richness**, which are crucial for producing high-quality TTS outputs.

---

## 1. Dataset Overview

| Dataset           | Duration | Speakers | Max Audio Length | Accent             | Notes                             |
| ----------------- | -------- | -------- | ---------------- | ------------------ | --------------------------------- |
| OpenSLR Bangla    | 11.2 hr  | 1        | 20 s             | Bangladeshi Bangla | Natural multi-sentence recordings |
| Google TTS Zephyr | 3 hr     | 1        | 20 s             | Bangladeshi Bangla | Synthetic, accent-focused         |
| **Total**         | 14.2 hr  | 2        | 20 s             | Bangladeshi Bangla | Hybrid dataset for fine-tuning    |

> Both datasets focus specifically on **Bangladeshi Bangla accent**, ensuring phonetic and prosodic consistency across the training data.

---

## 2. Lexical & Phonetic Coverage

* **Unique Words**: ~2,000 words across all datasets
* **Average Words per Sentence**: ~13 words
* **Phoneme Coverage**:

  * Natural and Google TTS data cover major phonemes in Bangladeshi Bangla.
  * Phonetic balance principles are inspired by the **SUST (Shahjalal University of Science and Technology) TTS Corpus**, ensuring that less frequent phonemes are adequately represented.
* **Accent Consistency**: Focused on **Bangladeshi Bangla pronunciation**, including subtle vowel and consonant variations and natural intonation patterns.

---

## 3. Audio Quality & Parameters

* **Recording Quality (OpenSLR)**: Clear, intelligible single-speaker recordings with minimal noise.
* **Synthetic Quality (Google TTS Zephyr)**: High-quality generated speech with consistent volume, pitch, and clarity.
* **Additional Parameters for Robustness**:

  * **Sample Rate**: 22.05 kHz
  * **Signal-to-Noise Ratio (SNR)**: High (>30 dB for natural recordings)
  * **Prosody Variation**: Diverse intonation and speech rhythm across datasets
  * **Max Clip Length**: 20 seconds
  * **Speaker Diversity**: Two speakers (1 natural, 1 synthetic)

---

## 4. Dataset Balance & Adequacy

* **Duration Ratio**: Natural recordings (~11.2 hr) dominate, synthetic (~3 hr) augments accent and pronunciation coverage.
* **Phonetic Coverage**: Principles from **SUST** ensure that major and minor phonemes in Bangladeshi Bangla are represented, improving model generalization.
* **Training Readiness**: Combined 14.2 hours of curated data provides **practical balance between quality and quantity** for VITS fine-tuning on Kaggle T4 GPUs.

---

## 5. Summary

* Total Duration: **14.2 hours**
* Speakers: **2** (1 natural, 1 synthetic)
* Max Audio Length: **20 s per clip**
* Unique Words: **~2,000**
* Average Words per Line: **13**
* Accent Focus: **Bangladeshi Bangla**
* Outcome: **High-quality, accent-consistent, phonetically balanced (inspired by SUST), and prosodically diverse dataset**, suitable for producing natural-sounding TTS outputs.

---

### Reference

* **SUST TTS Corpus**: Shahjalal University of Science and Technology. [Phonetically-Balanced Bangla TTS Corpus](file:///home/bs00728/Downloads/SUST_TTS_Corpus_A_phonetically-balanced_corpus_for.pdf)