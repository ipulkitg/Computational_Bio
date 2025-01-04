# Algorithms in Computational Biology – Project Repository

This repository contains six assignments completed for **CSE 494/559: Algorithms in Computational Biology (Fall 2024)** instructed by **Heewook Lee** at ASU. Each project explores foundational bioinformatics algorithms and computational methods for sequence alignment, pattern matching, motif discovery, hidden Markov models, and clustering.

> 📁 Each project has its own directory with detailed README, implementation code, and input/output samples.

---

## 📌 Project Index

### 🔬 Project 1: Exact Pattern Matching (Z-Algorithm)
- Implements the Z-algorithm for exact pattern matching in DNA sequences.
- Includes analysis on circular sequences and KMP variants.
- 📂 Folder includes: `main3.py`, test files, and a README.

---

### 🧬 Project 2: Motif Search (Randomized & Gibbs Sampling)
- Implements Randomized Motif Search and Gibbs Sampling for DNA motif discovery.
- Compares performance on synthetic datasets.
- 📂 Folder includes: `randomized_motiff.py`, `gibbs.py`, test sets, and README.

---

### 🧪 Project 3: Pairwise Sequence Alignment
- Global alignment with fixed gap penalty using BLOSUM62.
- Local alignment with affine gap penalties.
- 📂 Folder includes: `q1.py`, `q2.py`, and README.

---

### 📑 Project 4: Burrows-Wheeler Transform & Matching
- Constructs and inverts BWT.
- Implements LF Mapping and pattern search using BWT.
- 📂 Folder includes: `compute_BWT.py`, `reverse_BWT.py`, `lf_mapping.py`, and matching logic.

---

### 🔁 Project 5: Hidden Markov Models (HMM)
- Viterbi decoding, soft decoding, Viterbi learning, and Baum-Welch training.
- All probabilities computed in log-space.
- 📂 Folder includes: `viterbi.py`, `soft_decoding.py`, `param_using_viterbi.py`, and optional `baum_welch.py`.

---

### 📊 Project 6: Clustering (Optional)
- K-means clustering (hard) via Lloyd's Algorithm.
- Soft K-means clustering via EM with a stiffness parameter.
- 📂 Folder includes: `kmeans_hard.py`, `kmeans_soft.py`, and README.

---

## 🔧 How to Run
Each project folder includes:
- `README.md` with problem descriptions and sample input/output
- Scripts to execute the required algorithms
- Sample input files for testing

All programs are designed to run under **5 minutes** on standard machines.

---

## ⚠️ Notes
- All implementations were done from scratch based on class lectures.
- No external libraries used unless explicitly permitted.
- For academic integrity, all code adheres strictly to university guidelines.
