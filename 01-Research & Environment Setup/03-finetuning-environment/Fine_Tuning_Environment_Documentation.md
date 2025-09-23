# Fine-Tuning Environment Documentation

## Platform

* **Kaggle Notebooks** were used for model fine-tuning and experiments.
* Kaggle provides free access to GPUs, but with strict hardware and usage limits.

---

## Hardware Resources

### GPU

* **2 × NVIDIA Tesla T4 GPUs** per session.
* Each T4 GPU has:

  * ~15 GB VRAM (usable ~14.7–15.1 GB).
  * Tensor Cores optimized for **mixed precision (FP16)** acceleration.
* Suitable for lightweight models like **VITS**, but insufficient for **XTTS**, which typically requires **A100 GPUs (40–80 GB VRAM)**.

### CPU

* Multi-core CPUs (≈8 vCPUs allocated).
* CPU usage was minimal since GPU handled the majority of training.

### RAM

* **30 GB system RAM** per session.
* Training used ~5–6 GB, leaving headroom for preprocessing and dataloaders.

---

## Session Constraints

* **Maximum session length**: 12 hours (after which sessions are automatically terminated).
* **GPU weekly quota**: ~**30 hours per week** for free-tier users.
* After quota exhaustion, GPU access is suspended until reset.
* Frequent checkpointing was required to ensure training continuity across multiple sessions.

---

## Training Strategy in Kaggle

1. **Batch Size Adjustment**

   * Used **batch sizes of 1–2** due to limited VRAM.
   * Employed **gradient accumulation** to mimic larger batch training.

2. **Mixed Precision (fp16)**

   * Leveraged T4 Tensor Cores for faster training and reduced VRAM usage.

3. **Checkpointing**

   * Checkpoints saved every 2–3k steps.
   * Ensured safe resumption after session expiry or quota limits.

4. **Session Management**

   * Training spread across **multiple 12-hour sessions**.
   * Resumed from last saved checkpoint to continue fine-tuning without restarting from scratch.

---

## Why This Environment Fits VITS (But Not XTTS)

* **VITS**:

  * Compact, memory-efficient model.
  * Can be fine-tuned within Kaggle's **T4 GPU (15GB VRAM)** limit.
  * Works within **30 hours/week GPU quota**.

* **XTTS**:

  * Requires **A100 GPUs (80 GB VRAM)** and uninterrupted multi-day training runs.
  * Needs **thousands of GPU hours**, making it incompatible with Kaggle's free resource limits.

---

## Summary

The fine-tuning environment on Kaggle provided:

* **2 × NVIDIA Tesla T4 GPUs (15 GB VRAM each)**
* **30 GB RAM**
* **12-hour session limit**
* **~30 GPU hours per week quota**

This environment is well-suited for **VITS fine-tuning** but **infeasible for XTTS**, further justifying my model choice.