# K-Means Clustering

## Overview
This project implements the **K-Means Clustering Algorithm** from scratch without using pre-built machine learning libraries like Scikit-learn or NumPy. <br>
The primary objective is to cluster various datasets and analyze the error across different values of K (number of clusters). <br>

## Key Features
- **Manual Distance Calculation:** Implements Euclidean distance to compute the similarity between points. <br>
- **Random Initialization of Centroids:** Uses a fixed random seed to ensure reproducibility of results. <br>
- **Iterative Cluster Refinement:** The centroids are updated iteratively until convergence. <br>
- **Sum of Squared Errors (SSE):** Evaluates clustering quality using SSE, which is plotted against different K values. <br>
- **Comparison with Weka:** Accuracy of the custom K-Means implementation is compared with the Weka software’s built-in clustering algorithm.

'''bash
python 1002178072.py <dataset_file>
