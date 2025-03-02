import sys
import random
import matplotlib.pyplot as plt

# Reading the input Text File 
def read_data(filepath):
    data = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                values = list(map(float, line.strip().split()))
                data.append(values[:-1])      # Excluding the last column from the dataset i.e the class label  
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)         # Exit the program if the file is not found
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)        # Handle other potential errors that may occur during file reading
    return data

# Define Initial Centroids using Random Initalization
def select_initial_centroids(num_clusters, data):
    random.seed(0)   # Random state set to 0 to get reproducibility
    return random.sample(data, num_clusters)

# Calculate Euclidean Distance
def calculate_distance(point1, point2):
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

# Function that uses centroids to define data points for clusters
def define_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for idx, point in enumerate(data):
        distances = [calculate_distance(point, centroid) for centroid in centroids]
        closest_centroid_idx = distances.index(min(distances))
        clusters[closest_centroid_idx].append(idx)
    return clusters

def update_centroids(data, clusters):
    new_centroids = []
    for cluster in clusters:
        if not cluster:
            continue
        centroid = [sum(data[idx][dim] for idx in cluster) / len(cluster) for dim in range(len(data[0]))]
        new_centroids.append(centroid)
    return new_centroids

# Computing Error (SSE= Sum of Squared Errors)
def calculate_clustering_error(data, centroids, clusters):
    total_sse = 0
    for cluster, centroid in zip(clusters, centroids):
        for idx in cluster:
            distance = calculate_distance(data[idx], centroid)
            total_sse += distance ** 2      # Squaring the distance before adding to total
    return total_sse

# Defining k-means clustering algorithm
def perform_k_means(data, num_clusters, max_iterations=20):
    centroids = select_initial_centroids(num_clusters, data)
    for _ in range(max_iterations):
        clusters = define_clusters(data, centroids)
        new_centroids = update_centroids(data, clusters)
        if centroids == new_centroids:
            break
        centroids = new_centroids
    error = calculate_clustering_error(data, centroids, clusters)
    return error

# Plot Error vs K Graph
def plot_cluster_errors(k_values, errors):
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, errors, 'o-')
    plt.title('Error vs Number of Clusters (K)')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Error')
    plt.xticks(k_values)
    plt.grid(True)
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python 1002178072.py <data_file>")      # Update the path at runtime, if necessary
        sys.exit(1)

    data = read_data(sys.argv[1])
    k_range = range(2, 11)
    errors = [perform_k_means(data, k) for k in k_range]

    for k, error in zip(k_range, errors):
        print(f'For k = {k} After 20 iterations: Error = {error:.4f}')

    plot_cluster_errors(k_range, errors)

if __name__ == "__main__":
    main()

### Documentation: ###

# STudent Name: Kintur Ketan Shah
# Student ID: 1002178072
# Script Goal: This script implements the k-means clustering algorithm without the use of pre-built library functions.
# To run this code, enter the command 'python 1002178072.py <file_name>' in the terminal.
# Or the file path to the dataset can also be given in the string format (Ex: 'file_name.txt').
# It will take around 25 to 30 seconds to get output of this code as I have not used NumPy library anywhere.

# Random State: Set to 0, used a fixed random seed to ensure reproducibility of results.
# Results:
#  - After the final iteration, print the error for each (K).
#  - Shows an Error vs (K) plot to visualize the performance of algorithm with varying numbers of clusters.
# References: 
#   https://www.kaggle.com/code/adinishad/kmeans-clustering-from-scratch
#   https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
#   https://towardsdatascience.com/create-your-own-k-means-clustering-algorithm-in-python-d7d4c9077670
#   https://www.analyticsvidhya.com/blog/2021/01/in-depth-intuition-of-k-means-clustering-algorithm-in-machine-learning/
#   https://www.youtube.com/watch?v=5w5iUbTlpMQ
#   https://www.youtube.com/watch?v=MFraC1JObUo               