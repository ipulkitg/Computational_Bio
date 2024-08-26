# Project 3: Pairwise Sequence Alignment

This project implements two core algorithms for protein sequence alignment in bioinformatics: **Global Alignment with fixed gap penalty** and **Local Alignment with affine gap penalty**, using the BLOSUM62 substitution matrix.

## Algorithms Implemented

### 1. Global Alignment (Needleman-Wunsch Algorithm)
- Uses a fixed gap penalty: σ = 5
- Uses BLOSUM62 for substitution scoring.
- Outputs the global alignment and its score.

**Input Format**:
- FASTA-style input:
```
>Sequence 1
WKMDKSYWLFVREKKTDLCM
>Sequence 2
AIDDKSWAFVRECKTDQTW
```

**Sample Output**:
```
40
WKMDKSYWLFVREKKTDLCM
AIDDKS-WAFVRECKTDQTW
```

---

### 2. Local Alignment (Smith-Waterman Algorithm)
- Uses affine gap penalty:
  - Gap opening penalty σ = 11
  - Gap extension penalty ε = 1
- Uses BLOSUM62 for substitution scoring.
- Outputs the score and aligned substrings (not the alignment itself).

**Sample Output**:
```
47
DKSYWLFVREKKTD
DKSWAFVRECKTD
```

---

## Notes

- Implementations are optimized to run within 5 minutes wall time.
- BLOSUM62 scoring matrix is used from:  
  [NCBI BLOSUM62](https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt)

- Developed as part of *CSE 494/559: Algorithms in Computational Biology - Fall 2024*.
