import sys
import math


def read_input():
    """Reads input data from stdin and rounds the values."""
    input_lines = sys.stdin.readlines()
    k, m = map(int, input_lines[0].strip().split())
    data_points = [list(map(lambda x: round(float(x), 6), line.strip().split())) for line in input_lines[1:]]
    return k, m, data_points


def euclidean_distance(point1, point2):
    """Computes the Euclidean distance between two points."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


def assign_clusters(data_points, centers):
    """Assigns each data point to the nearest cluster center."""
    clusters = [[] for _ in range(len(centers))]
    for point in data_points:
        distances = [euclidean_distance(point, center) for center in centers]
        cluster_idx = distances.index(min(distances))
        clusters[cluster_idx].append(point)
    return clusters


def compute_new_centers(clusters, centers, m):
    """Computes new cluster centers as the mean of points in each cluster."""
    new_centers = []
    for i, cluster in enumerate(clusters):
        if cluster:  # If the cluster has points, compute the mean
            new_center = [
                round(sum(coord[j] for coord in cluster) / len(cluster), 6)
                for j in range(m)
            ]
        else:  # If the cluster is empty, retain the previous center
            new_center = centers[i]
        new_centers.append(new_center)
    return new_centers


def has_converged(old_centers, new_centers):
    """Checks if the algorithm has converged (centers do not change)."""
    return all(
        all(round(old_centers[i][j], 6) == round(new_centers[i][j], 6) for j in range(len(old_centers[i])))
        for i in range(len(old_centers))
    )


def kmeans_clustering(k, m, data_points):
    """Implements Lloyd's Algorithm for K-means clustering."""
    # Initialize centers as the first k data points
    centers = data_points[:k]
    
    while True:
        # Assign points to clusters
        clusters = assign_clusters(data_points, centers)
        
        # Compute new centers
        new_centers = compute_new_centers(clusters, centers, m)
        
        # Check for convergence
        if has_converged(centers, new_centers):
            break
        
        centers = new_centers
    
    return centers


def main():
    k, m, data_points = read_input()
    centers = kmeans_clustering(k, m, data_points)
    for center in centers:
        print(" ".join(f"{round(coord, 3):.3f}" for coord in center))


if __name__ == "__main__":
    main()