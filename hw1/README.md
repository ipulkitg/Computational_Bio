# Project 1: Exact Pattern Matching using Z-Algorithm

This project implements the Z-algorithm for exact pattern matching in DNA sequences, where both the text `t` and pattern `p` are over the alphabet Σ = {A, C, G, T}, with |p| ≤ |t|.

## Features

- Custom implementation of the Z-algorithm from scratch.
- Finds all occurrences of `p` in `t` (1-based indexing).
- Outputs match positions in ascending order.
- Reports total comparisons, matches, and mismatches.

## Input Format

A plain text file with:
- Line 1: DNA sequence `t`
- Line 2: DNA pattern `p`

### Example
```
ACAGTATCAGTACAG
CAG
```

## Sample Output
```
2
8
13
Number of comparisons: 18
Number of matches: 9
Number of mismatches: 11
```

## Additional Questions

- **Biological Application**: Describes how the Z-algorithm can verify if two linear sequences come from the same circular DNA.
- **KMP Analysis**: Evaluates a proposed modification to the KMP algorithm using `lps'`.
- **(Optional)**: Pseudocode to compute modified `lps'` using Z-array values.

## Notes

- Full credit requires implementing Z-algorithm manually.
- Assignment from *CSE 494/559: Algorithms in Computational Biology, Fall 2024*.
