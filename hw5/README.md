# Project 5: Hidden Markov Models (HMM)

This project implements core algorithms involving **Hidden Markov Models (HMM)**, including the Viterbi algorithm, parameter estimation, soft decoding, and Baum-Welch learning. All probabilities are computed in **log space** to prevent underflow.

## Implemented Modules

### 1. Viterbi Algorithm (60 pts)
Finds the most likely sequence of hidden states π that maximizes Pr(x, π).

**Input**:
- Observed sequence `x`
- Alphabet Σ
- List of hidden states
- Transition matrix `T`
- Emission matrix `E`

**Output**: Most probable hidden path

**Example**:
```
Input:  xyxzzxyxyy ...
Output: AAABBAAAAA
```

---

### 2. Viterbi Learning (60 pts)
Estimates HMM parameters (T, E) to maximize Pr(x, π) over all possible parameter sets using Viterbi paths.

**Input**:
- Number of iterations
- Observed sequence `x`
- Alphabet, states, initial `T` and `E`

**Output**: Updated transition and emission matrices

---

### 3. Soft Decoding (60 pts)
Computes Pr(Π_i = k | x) for each hidden state `k` at each step `i`, indicating the probability the HMM was in state `k` when emitting symbol `x_i`.

**Output**: Matrix of conditional probabilities per step per state

---

### 4. Baum-Welch Learning (60 pts, Optional for 494)
An Expectation-Maximization (EM) approach that updates HMM parameters by using both node and edge soft decoding.

**Output**: Optimized `T` and `E` matrices after multiple EM iterations

---

## Notes
- All algorithms must run within 5 minutes (wall time)
- Initial probabilities are assumed to be uniformly distributed
- Implemented for *CSE 494/559: Algorithms in Computational Biology – Fall 2024*
