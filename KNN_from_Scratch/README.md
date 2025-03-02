# K-Nearest Neighbors (KNN) from Scratch for Text Classification

### This project demonstrates an implementation of the K-Nearest Neighbors (KNN) algorithm from scratch without using machine learning libraries such as Scikit-learn. The goal is to apply the KNN algorithm to classify text data and gain an in-depth understanding of how the algorithm works at a fundamental level.

🚀 **Project Overview**
Implementation: Built entirely from scratch, with manual computation of distances and neighbor selection. <br>
Datasets: The project uses three different textual datasets to evaluate the performance of the KNN algorithm.

📂 **Repository Structure:**
KNN_from_Scratch/: Contains the KNN implementation and 3 dataset files. <br>
knn.ipynb: Jupyter Notebook for implementing the KNN algorithm from scratch. <br>
README.md: Project description and instructions.

🔑 **Key Features:** <br>
**Manual Distance Calculation:** Implements Euclidean or Cosine distance from scratch to find the k-nearest neighbors. <br>
**Text Preprocessing:** Tokenizes and vectorizes the text data before applying the KNN algorithm. <br>
**Multi-Dataset Evaluation:** The algorithm is evaluated on three different datasets to assess its performance and versatility. <br>
**Classification:** Predicts the label of the input text data based on majority voting from the nearest neighbors. 

📈 **Future Enhancements:** <br>
Add cross-validation to improve model evaluation. <br>
Explore optimization techniques for handling larger datasets efficiently.

## Accuracy Comparison with Weka:
To evaluate the effectiveness of the custom-built KNN model, **Weka** is used as a benchmark tool for accuracy comparison. 

### What is Weka?
[Weka](https://www.cs.waikato.ac.nz/ml/weka/) (Waikato Environment for Knowledge Analysis) is an open-source machine learning software written in Java. It provides various tools for data preprocessing, classification, clustering, regression, and visualization. Weka's built-in KNN classifier (IBk) is used to validate the accuracy of the custom implementation.
