# Project 4: Multiple Pattern Matching using Burrows-Wheeler Transform (BWT)

This project implements multiple pattern matching techniques based on the **Burrows-Wheeler Transform (BWT)** and its associated algorithms. The goal is to construct efficient pattern matchers for a given text using various BWT-based transformations and mappings.

## Implemented Modules

### 1. Compute BWT (20 pts)
Generates the Burrows-Wheeler Transform of a string by:
- Generating all cyclic rotations.
- Sorting them lexicographically.
- Returning the last column of the sorted rotations.

**Input**: A string `s` ending with `$`  
**Output**: The BWT of `s`

**Example**:
```
Input:  panamabananas$
Output: smnpbnnaaaaa$a
```

---

### 2. Inverse BWT (20 pts)
Reconstructs the original string from a given BWT.

**Input**: BWT string `t` (with one `$`)  
**Output**: Original string

**Example**:
```
Input:  smnpbnnaaaaa$a
Output: panamabananas$
```

---

### 3. LF Mapping (25 pts)
Implements the **Last-to-First (LF) Mapping**:
- For a character at index `i` in the BWT, it finds the corresponding index in the first column of the BWM.

**Input**: BWT string and index `i`  
**Output**: Index in the first column corresponding to the `i`-th character in BWT

**Example**:
```
Input:  smnpbnnaaaaa$a
        2
Output: 9
```

---

### 4. Burrows-Wheeler Matching (35 pts)
Implements the BWT Matching algorithm:
- Matches patterns from right to left using LF Mapping.
- For each pattern, outputs the number of occurrences in the original text.

**Input**: BWT string and list of space-separated patterns  
**Output**: Frequency count for each pattern

**Example**:
```
Input:  smnpbnnaaaaa$a
        ana na nam nas nab
Output: 3 3 1 1 0
```

---

## Notes
- Programs must complete within 5 minutes (wall time).
- Developed for *CSE 494/559: Algorithms in Computational Biology – Fall 2024*.
