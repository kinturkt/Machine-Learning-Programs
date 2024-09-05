This project demonstrates an implementation of the K-Nearest Neighbors (KNN) algorithm from scratch without using machine learning libraries such as Scikit-learn. The goal is to apply the KNN algorithm to classify text data and gain an in-depth understanding of how the algorithm works at a fundamental level.

🚀 Project Overview
Algorithm: K-Nearest Neighbors (KNN)
Task: Text classification
Implementation: Built entirely from scratch, with manual computation of distances and neighbor selection.
Datasets: The project uses three different textual datasets to evaluate the performance of the KNN algorithm.

📂 Repository Structure
KNN_from_Scratch/: Contains the KNN implementation and dataset files.
knn.py: Python script implementing the KNN algorithm from scratch.
README.md: Project description and instructions.

🔑 Key Features
Manual Distance Calculation: Implements Euclidean or Cosine distance from scratch to find the k-nearest neighbors.
Text Preprocessing: Tokenizes and vectorizes the text data before applying the KNN algorithm.
Classification: Predicts the label of the input text data based on majority voting from the nearest neighbors.

📈 Future Enhancements
Add cross-validation to improve model evaluation.
Explore optimization techniques for handling larger datasets efficiently.
