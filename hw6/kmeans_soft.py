import sys
import math


def read_input():
    """Reads input data from stdin."""
    input_lines = sys.stdin.readlines()
    k, m = map(int, input_lines[0].strip().split())
    data_points = [list(map(float, line.strip().split())) for line in input_lines[1:]]
    return k, m, data_points


def euclidean_distance(point1, point2):
    """Computes the Euclidean distance between two points."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


def assign_clusters(data_points, centers):
    """Assigns each data point to the nearest cluster center."""
    clusters = [[] for _ in range(len(centers))]
    for point in data_points:
        distances = [euclidean_distance(point, center) for center in centers]
        # If there is a tie, the first center is chosen
        cluster_idx = distances.index(min(distances))
        clusters[cluster_idx].append(point)
    return clusters


def compute_new_centers(clusters, centers, m):
    """Computes new cluster centers as the mean of points in each cluster."""
    new_centers = []
    for i, cluster in enumerate(clusters):
        if cluster:  # If the cluster has points, compute the mean
            new_center = [sum(coord[j] for coord in cluster) / len(cluster) for j in range(m)]
        else:  # If the cluster is empty, retain the previous center
            new_center = centers[i]
        new_centers.append(new_center)
    return new_centers


def has_converged(old_centers, new_centers, threshold=1e-9):
    """Checks if the algorithm has converged (centers do not change)."""
    return all(
        all(abs(old_centers[i][j] - new_centers[i][j]) < threshold for j in range(len(old_centers[i])))
        for i in range(len(old_centers))
    )


def kmeans_clustering(k, m, data_points):
    """Implements Lloyd's Algorithm for K-means clustering."""
    # Initialize centers as the first k data points
    centers = data_points[:k]
    iteration = 0  # To track the iteration number
    
    while True:
        print(f"Iteration {iteration}:")
        print(f"Current centers: {centers}")
        
        # Assign points to clusters
        clusters = assign_clusters(data_points, centers)
        print(f"Clusters: {clusters}")
        
        # Compute new centers
        new_centers = compute_new_centers(clusters, centers, m)
        print(f"New centers: {new_centers}")
        
        # Check for convergence
        if has_converged(centers, new_centers):
            print(f"Convergence reached after {iteration} iterations.")
            break
        
        centers = new_centers
        iteration += 1
    
    return centers


def main():
    k, m, data_points = read_input()
    centers = kmeans_clustering(k, m, data_points)
    for center in centers:
        print(" ".join(f"{coord:.3f}" for coord in center))


if __name__ == "__main__":
    main()