# Adult_Income_Prediction
Welcome to the Adult Income Prediction project! This project uses machine learning techniques to classify individuals' income levels based on demographic and employment-related attributes. The goal is to predict whether a person earns more than $50K a year.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
4. [Feature Engineering](#feature-engineering)
5. [Models](#models)
    - [Logistic Regression](#logistic-regression)
    - [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
    - [Support Vector Machine (SVM)](#support-vector-machine-svm)
6. [Model Comparison](#model-comparison)
7. [Conclusion](#conclusion)
8. [About Me](#about-me)
9. [License](#license)

## Introduction

<img src="https://github.com/Fatma-Nur-Azman/Machine_Learning_Projects_ML/blob/main/ML_04_Adult_Income_Prediction/adult_.png">

## Dataset

- **Source:** UCI Machine Learning Repository
- **Rows:** 32,561
- **Columns:** 15
- **Attributes:** 
    - Age, Workclass, fnlwgt, Education, Education Number, Marital Status, Occupation, Relationship, Race, Sex, Capital Gain, Capital Loss, Hours per Week, Native Country, Income

## Exploratory Data Analysis (EDA)

The EDA section includes:
- **Understanding The Data:** Basic statistics and distribution analysis.
- **Handling Missing Values:** Imputing or removing missing values.
- **Detection of Outliers:** Identifying and handling outliers in the data.
- **Correlation Analysis:** Exploring the relationships between different numerical features.

## Feature Engineering

Various feature engineering steps were performed, such as:
- **Categorical Features:** Encoding categorical variables using OneHotEncoder and OrdinalEncoder.
- **Numerical Features:** Scaling numerical variables using StandardScaler.
- **Feature Creation:** Creating new features from existing ones to enhance model performance.


## Models

### Logistic Regression
A Logistic Regression model was built and optimized using GridSearchCV to predict the income level. The model was evaluated using confusion matrices, ROC curves, and precision-recall curves.

### K-Nearest Neighbors (KNN)
A KNN model was applied, and the optimal number of neighbors was selected using the Elbow Method. The model was evaluated with similar metrics as Logistic Regression.

### Support Vector Machine (SVM)
The SVM model was trained using different kernels, and hyperparameters were tuned using GridSearchCV. Performance metrics include confusion matrices, ROC curves, and precision-recall curves.

## Model Comparison

The performance of all models was compared based on metrics such as accuracy, precision, recall, and F1-score. The results were visualized using confusion matrices, ROC curves, and precision-recall curves.

## Conclusion

The project concludes by summarizing the performance of each model and discussing potential improvements and future work.

## About Me

Hello! I'm Dikshant Pareshkumar Patel, a data analytics and data science enthusiast.

📊 Data Explorer: I dive into data to uncover insights. Analyzing data and finding patterns is my zone of genius!

☕ Coffee Aficionado: Coffee fuels my focus while I work with data—each sip sparks creativity and energy.

🎶 Jazz Fan: Soft jazz plays as I code, keeping my mind focused and my mood inspired.

🧩 Puzzle Solver: I tackle puzzles to keep my analytical skills sharp. It’s my favorite brain workout.

💡 Daily Algorithm Practice: Every day, I solve an algorithm challenge. It’s my way of staying sharp and learning new techniques.

📧 Contact

- [LinkedIn](https://www.linkedin.com/in/dikshantp2210/)
- [GitHub](https://github.com/DikshantPatel2210)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Ready to embark on a journey in the world of machine learning with raisins? 🍇🚀 If you find this repository helpful, don't forget to ⭐ star it!

Happy Coding! 💻✨
