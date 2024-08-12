# Project 2: Motif Search using Randomized and Gibbs Sampling Algorithms

This project implements two popular algorithms used in computational biology for motif discovery in DNA sequences: **Randomized Motif Search** and **Gibbs Sampling**. Both methods use probabilistic strategies to iteratively refine motif sets based on sequence profiles.

## Algorithms Implemented

### 1. Randomized Motif Search
- Initializes with a randomly selected motif set.
- Iteratively updates motif set using profiles with pseudocounts.
- Repeats the process 1500 times to report the best-scoring motif set.

**Input Format**:
- Line 1: Two integers, `k` (motif length) and `t` (number of DNA sequences).
- Next `t` lines: DNA sequences.

**Sample Input**:
```
7 5
TAAAACACATTTTTCTCCAGTCGGGATTAAG
TTATGTTCGCTCTCGGTCTAAGGTTCTAAGT
GTCGAATGTGAATGGGTGGTCGCGAGTTATC
GTGCAGGTCCCAGTTCTAGATCATTCTGGAA
GCAAGAAGTACAAGATCTAGGCTCCTTAACG
```

### 2. Gibbs Sampling
- Starts with random motifs and iteratively samples one sequence to refine motifs based on profile excluding it.
- Runs 30 independent trials to find the best motif set.

**Input Format**:
- Line 1: Three integers, `k`, `t`, and `r` (number of iterations).
- Next `t` lines: DNA sequences.

**Sample Input**:
```
7 5 100
TAAAACACATTTTTCTCCAGTCGGGATTAAG
TTATGTTCGCTCTCGGTCTAAGGTTCTAAGT
GTCGAATGTGAATGGGTGGTCGCGAGTTATC
GTGCAGGTCCCAGTTCTAGATCATTCTGGAA
GCAAGAAGTACAAGATCTAGGCTCCTTAACG
```

## Output
A list of `t` best motifs, one per line.

## Additional Task
- Compare both algorithms on a provided motif dataset (`k=15`) using multiple iteration counts.
- Report consensus sequences, scores, and discuss convergence behavior and result quality.

## Notes
- Make sure to include pseudocounts when building profiles.
- Developed as part of *CSE 494/559: Algorithms in Computational Biology - Fall 2024*.
