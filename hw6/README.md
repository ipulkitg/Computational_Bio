# Project 6: Clustering Algorithms

This project explores both **hard** and **soft** K-means clustering techniques. You will implement Lloyd’s algorithm for hard clustering and an Expectation-Maximization (EM) approach for soft clustering using a statistical partition function.

> ⏱️ Note: All implementations must complete within 5 minutes (wall time).

## Implemented Algorithms

### 1. Lloyd's Algorithm (Hard K-means) – 60 pts
An iterative clustering algorithm that alternates between assigning data points to the nearest center and updating centers to be the mean of assigned points.

**Input Format**:
- Line 1: `k` (clusters) and `m` (dimensions)
- Next `n` lines: m-dimensional data points

**Sample Input**:
```
2 2
1.3 1.1
1.3 0.2
...
```

**Sample Output**:
```
1.800 2.867
1.060 1.140
```

---

### 2. Soft K-means via EM Algorithm – 40 pts
Uses soft assignment of data points to clusters via responsibilities, influenced by a stiffness parameter β. Centers are updated using weighted contributions from all points.

**Input Format**:
- Line 1: `k` and `m`
- Line 2: stiffness parameter `β`
- Next `n` lines: m-dimensional data points

**Sample Input**:
```
2 2
2.7
1.3 1.1
1.3 0.2
...
```

**Sample Output**:
```
1.662 2.623
1.075 1.148
```

---

## Notes
- All clustering is done in Euclidean space.
- Use statistical physics–based partition function for soft clustering.
- Developed as part of *CSE 494/559: Algorithms in Computational Biology – Fall 2024*.
