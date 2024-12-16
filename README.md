# Healthe Disease Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fphealthdiseaseprediction.streamlit.app/)

This project demonstrates the application of modeling and simulation techniques for predicting health risks. It explores synthetic health datasets, performs statistical analyses, and develops predictive machine learning models. The interactive web application allows users to load datasets, visualize data, and evaluate machine learning models.

## Overview
This project aims to provide insights into understanding and managing health risks effectively. It is designed as a step-by-step interactive tool to:
1. Explore health-related datasets.
2. Train and evaluate machine learning models.
3. Visualize data relationships.

## Features
- **Dataset Exploration**: Load, clean, and preview datasets.
- **Model Training and Evaluation**: Select and train models such as Random Forest, Logistic Regression, and Gradient Boosting.
- **Interactive Visualizations**: Generate pairplots and correlation heatmaps.
- **Feature Importance Analysis**: Display the importance of features for tree-based models.

## Usage
1. Launch the app using Streamlit.
2. Select a dataset from the dropdown menu.
3. Explore dataset details, including shape and attributes.
4. Visualize data relationships using pairplots and heatmaps.
5. Select a machine learning model, train it, and view the evaluation metrics.
6. Analyze feature importance for tree-based models.

## Datasets
The following datasets are used:

### 1. Heart Disease
- **Description**: Diagnoses of heart disease based on 14 attributes.
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)

### 2. Diabetes
- **Description**: PIMA Indian diabetes dataset.
- **Source**: [UCI Machine Learning Repository]((https://archive.ics.uci.edu/dataset/34/diabetes))

### 3. Breast Cancer
- **Description**: Wisconsin Diagnostic Breast Cancer (WDBC) dataset.
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))

### 4. Liver Disorders
- **Description**: Dataset for liver disorder diagnoses.
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Liver+Disorders)

## Machine Learning Models
The following models are supported:
- **Random Forest Classifier**
- **Logistic Regression**
- **Gradient Boosting Classifier**

### Evaluation Metrics
- **Accuracy**: Overall performance of the model.
- **Classification Report**: Precision, recall, F1-score, and support for each class.

## Visualization Tools
- **Pairplot**: Explore relationships between variables.
- **Correlation Heatmap**: Identify correlations between features.
- **Feature Importance**: Analyze the importance of features for tree-based models.

---

Created by May Angeline as part of the CSEC 413: Modeling and Simulation Final Project.
