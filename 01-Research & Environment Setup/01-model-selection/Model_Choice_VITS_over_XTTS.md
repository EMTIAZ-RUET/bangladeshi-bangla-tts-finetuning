# Model Choice: VITS over XTTS

For this assignment, I have chosen **VITS** instead of **XTTS**.
While XTTS is a stronger architecture with advanced zero-shot multilingual capabilities, it is **not practical under the GPU and time constraints** of this task. Below I provide a detailed justification.

---

## 1. GPU and Compute Constraints

**XTTS (BnTTS by Verbex.ai)**

* The **BnTTS paper (Verbex.ai, 2025)** demonstrates the massive compute requirements for training XTTS in Bangla:

  * *"We continuously pre-trained the BnTTS model (initialized from the XTTS checkpoint) on **3.85k hours of Bengali speech data**, sourced from open-source datasets, pseudo-labeled data, and synthetic datasets."*
  * *"All experiments are run on a **single NVIDIA A100 GPU with 80GB VRAM**."*
  * *"The vocoder was fine-tuned for three days to ensure optimal performance."*
* These requirements (multi-thousand-hour datasets, 80GB VRAM GPUs, multi-day training runs) are **impossible to reproduce** on free or lightweight environments such as Kaggle or Colab, which typically provide 12–16GB VRAM GPUs.

**VITS**

* Lightweight and trainable on **12–16GB VRAM GPUs** with:

  * Small batch sizes (1–2).
  * Gradient accumulation.
  * Mixed precision (fp16) to reduce memory usage.
* Already has **open-source Bangla-pretrained checkpoints**, making adaptation feasible on resource-constrained platforms.

---

## 2. Time Constraints

* The assignment duration is **5 days**.
* XTTS training, as reported in the Verbex.ai work, required:

  * **3.85k hours of pretraining data**.
  * **Multi-day GPU training** (including vocoder fine-tuning alone taking three days).
* Even with access to enterprise GPUs, reproducing this pipeline would take **weeks**, not days.
* In contrast, **VITS fine-tuning can be demonstrated in hours**:

  * Typical Colab/Kaggle runs take **1–2 hours** per experiment.
  * This allows multiple iterations within the 5-day timeframe to explore fine-tuning, evaluation, and deployment.

---

## 3. Availability of Pretrained Models

* **XTTS**: No **Bangla XTTS checkpoints** are publicly available. Reproducing Verbex.ai's results would require their proprietary datasets and compute infrastructure.
* **VITS**: Multiple **Bangla-pretrained checkpoints** (e.g., `bangla-speech-processing/bangla_tts_female`) are openly available on HuggingFace, making it the practical choice for rapid fine-tuning.

---

## 4. Comparative Summary

| Factor                    | XTTS (BnTTS, Verbex.ai)                                                    | VITS (Chosen)                                |
| ------------------------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| **Dataset Size Needed**   | *"Pre-trained on **3.85k hours of Bengali speech data***"                  | 50–100 hours sufficient for fine-tuning      |
| **GPU Requirement**       | *"All experiments are run on a **single NVIDIA A100 GPU with 80GB VRAM***" | 12–16GB VRAM (Colab/Kaggle feasible)         |
| **Training Strategy**     | Multi-stage continual pretraining + vocoder fine-tuning (3 days)           | Direct fine-tuning of pretrained Bangla VITS |
| **Pretrained Models**     | No Bangla XTTS checkpoint available                                        | Multiple Bangla-pretrained checkpoints exist |
| **Timeline Fit (5 days)** | Unrealistic (multi-week training)                                          | Feasible (hours to days per experiment)      |

---

## References

1. **Assignment Instructions** – *AI/ML Engineer Assignment - TTS: Bangladeshi Bangla TTS Fine-Tuning*
2. **BnTTS (Verbex.ai)** – *BnTTS: Few-Shot Speaker Adaptation in Low-Resource Setting* (2025):

   * *"We continuously pre-trained the BnTTS model (initialized from the XTTS checkpoint) on **3.85k hours of Bengali speech data**..."*
   * *"All experiments are run on a **single NVIDIA A100 GPU with 80GB VRAM**."*
   * *"The vocoder was fine-tuned for three days to ensure optimal performance."*

---

## Final Justification

I selected **VITS** over XTTS because of **realistic compute and time constraints**:

* XTTS (BnTTS) required **3,856 hours of data** and training on **A100 GPUs with 80GB VRAM**, making it infeasible in my environment.
* The assignment timeline of **5 days** rules out XTTS, which would take weeks to train even with high-end infrastructure.
* VITS is **lightweight, reproducible, and already has Bangla-pretrained checkpoints**, enabling me to fine-tune effectively on Colab/Kaggle and focus on the assignment's goals: accent adaptation, evaluation, and deployment.

---

**Note:** This decision prioritizes practical implementation and reproducibility within the given constraints while still achieving the core objectives of Bangladeshi Bangla TTS fine-tuning.