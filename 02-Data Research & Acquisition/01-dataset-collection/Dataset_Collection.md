# Dataset Collection

For this fine-tuning task, I adopted a **hybrid dataset collection strategy** by combining **open-source Bangla speech data** with **synthetically generated Bangladeshi Bangla speech**. This approach balances **linguistic diversity, audio quality, and accent adaptation**, which are critical for building a robust Bangladeshi Bangla TTS system.

---

## 1. OpenSLR Bangla (HuggingFace Hosted)

* **Source**: [intelsense/openslr-bangla](https://huggingface.co/datasets/intelsense/openslr-bangla/viewer?views%5B%5D=train)
* **Description**:

  * Based on OpenSLR resources, this dataset contains recorded Bangla speech paired with transcripts.
  * Covers a wide range of Bangla sentences with natural prosody and varied speakers.
  * Features **Bangladeshi Bangla accent**.
* **Role in Training**:

  * Served as the **core dataset** for fine-tuning.
  * Provided **authentic phonetic and prosodic diversity**, ensuring natural-sounding outputs.

---

## 2. Google TTS – Zephyr (Bangladeshi Bangla Version)

* **Source**: Google Cloud Text-to-Speech (Zephyr voice, Bangladeshi accent)
* **Description**:

  * Generated **synthetic audio data** using the Bangladeshi variant of Google TTS.
  * Ensured coverage of **Bangladeshi-specific pronunciation, intonation, and lexical differences**.
* **Why Synthetic Data?**

  * Synthetic TTS allows inclusion of **controlled Bangladeshi-accented speech**, complementing the natural dataset.
* **Role in Training**:

  * Used as an **augmentation dataset**.
  * Introduced controlled, accent-specific data into the training set.
  * Helped the model learn **Bangladeshi-specific phoneme realizations** (subtle vowel/consonant variations).

---

## 3. Hybrid Dataset Strategy

The combined dataset was constructed with the following principles:

* **Authenticity + Adaptation**

  * OpenSLR Bangla ensures natural speech variety.
  * Google TTS Zephyr provides **targeted Bangladeshi accent adaptation**.

* **Coverage + Control**

  * OpenSLR offers diverse speaker voices.
  * Synthetic Zephyr provides controlled generation for local linguistic patterns.

* **Resource Awareness**

  * Instead of collecting thousands of hours of raw data (as done by larger TTS projects), a **smaller, curated dataset** was created.
  * This dataset is **feasible to train on Kaggle's T4 GPUs** within a **5-day assignment window**.

---

## 4. Summary

* **Primary Dataset**: [OpenSLR Bangla (HuggingFace)](https://huggingface.co/datasets/intelsense/openslr-bangla/viewer?views%5B%5D=train)

  * Natural recordings, multi-speaker, linguistically diverse, **Bangladeshi Bangla accent**.

* **Augmentation Dataset**: Google TTS Zephyr (Bangladeshi version)

  * Synthetic, accent-focused, controlled data.

* **Outcome**:

  * Created a **balanced dataset** preserving natural phonetic diversity while adapting the model toward **Bangladeshi Bangla speech patterns**.
  * Enabled **VITS fine-tuning within Kaggle constraints** (15 GB VRAM GPUs, 30-hour weekly GPU quota, 12-hour session limit).

---

## 5. Optional Dataset Statistics (Recommended)

| Dataset           | #Hours | #Samples | Accent             | Notes                             |
| ----------------- | ------ | -------- | ------------------ | --------------------------------- |
| OpenSLR Bangla    | XX     | XXX      | Bangladeshi Bangla | Natural recordings, multi-speaker |
| Google TTS Zephyr | XX     | XXX      | Bangladeshi Bangla | Synthetic, accent-focused         |
| **Total**         | XX     | XXX      | Mixed              | Hybrid, fine-tuning ready         |

> Note: Replace `XX` and `XXX` with actual counts after preprocessing.