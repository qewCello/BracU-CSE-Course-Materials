# 🧠 RAM Price Range Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the price range of computer RAM modules using hardware specifications collected from real-world eBay listings.

The project compares five supervised learning algorithms, performs hyperparameter optimization, evaluates multiple performance metrics, and deploys the best-performing model through a Flask web application.

---

## 📌 Project Overview

Online marketplaces such as eBay contain thousands of RAM products with varying specifications and prices.

Instead of predicting the exact price, this project formulates the task as a **multi-class classification** problem by categorizing RAM into:

- 💰 Budget
- 💎 Mid-Range
- 🚀 Premium

The objective is to identify the most appropriate price category from hardware specifications.

---

## Features

- Data preprocessing pipeline
- Missing value handling
- Feature encoding
- Class balancing using SMOTE
- Feature engineering
- Hyperparameter tuning
- Comparison of multiple ML models
- Performance visualization
- Flask REST API
- Interactive web interface

---

# Dataset

Source:

**Kaggle - RAM Pricing Dataset (2026 eBay Listings)**

Dataset Characteristics

- 2,899 records
- 17 features
- 149 RAM brands
- DDR4 & DDR5 memory
- Capacities from 8GB to 192GB

Features include:

- RAM Capacity
- RAM Generation
- Brand
- Speed
- Number of Modules
- Seller Information
- Hardware Specifications
- Market-related attributes

---

# Machine Learning Models

The following models were implemented and compared:

| Model | Purpose |
|--------|----------|
| Logistic Regression | Linear baseline classifier |
| Decision Tree | Tree-based classification |
| Random Forest | Ensemble learning |
| Multi-Layer Perceptron | Deep Neural Network |
| Support Vector Machine | Margin-based classifier |

---

# Data Preprocessing

The preprocessing pipeline includes:

- Removing unnecessary columns
- Missing value treatment
- One-Hot Encoding
- Label Encoding
- Feature scaling
- SMOTE oversampling
- Train/Test split

---

# Hyperparameter Optimization

Each model was tuned using multiple parameter combinations.

Examples include:

### Logistic Regression

- C = 0.01
- C = 0.1
- C = 10
- C = 1000

### Decision Tree

- Maximum Depth
- Minimum Leaf Size

### Random Forest

- Number of Trees
- Maximum Depth

### Multi-Layer Perceptron

- Hidden Layer Sizes
- Activation Functions
- Optimizers

### Support Vector Machine

- Linear Kernel
- RBF Kernel
- Different C values

---

# Model Performance

| Model | Accuracy | F1 Score |
|--------|----------|----------|
| Logistic Regression | 86.04% | 0.8602 |
| Decision Tree | 86.04% | 0.8610 |
| Random Forest | 86.21% | 0.8618 |
| MLP | 86.21% | 0.8622 |
| **Support Vector Machine** | **86.39%** | **0.8635** |

## 🏆 Best Model

Support Vector Machine (SVM)

Performance:

- Accuracy: **86.39%**
- Precision: **0.8635**
- Recall: **0.8639**
- F1 Score: **0.8635**
- ROC-AUC: **0.9454**

---

# Evaluation Metrics

The project evaluates each model using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Precision-Recall Curve
- Learning Curve
- Calibration Curve

---

# System Architecture

Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

SMOTE

↓

Model Training

↓

Hyperparameter Tuning

↓

Model Evaluation

↓

Best Model Selection (SVM)

↓

Flask API

↓

Web Application

---

# Flask API

The trained SVM model is exported as a `.pkl` file and served using Flask.

Example endpoint:

```
POST /api/predict
```

Input:

```json
{
  "ram_capacity": 32,
  "generation": "DDR5",
  "speed": 6000,
  ...
}
```

Output:

```json
{
  "price_range": "Premium"
}
```

---

# Project Structure

```
RAMprice/
│
├── app.py
├── ram_price_model.pkl
├── requirements.txt
├── render.yaml
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── notebooks/
│
├── dataset/
│
└── README.md
```

---

# Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Flask
- HTML
- CSS
- JavaScript

---

# Results

The comparison demonstrates that Support Vector Machine produced the best balance between precision, recall, and F1 score while maintaining excellent generalization performance.

The trained model was successfully deployed through a Flask web application, allowing users to predict RAM price categories in real time.

---

# Future Improvements

- Transformer-based tabular models
- XGBoost and LightGBM comparison
- Explainable AI using SHAP
- Real-time eBay API integration
- Continuous model retraining
- Docker deployment
- Cloud hosting

---

# Author

**Ayasha Islam**

Department of Computer Science & Engineering

BRAC University

Interested in:

- Machine Learning
- Artificial Intelligence
- NLP
- Product & Technology
- Data Science

---

# Citation

If you use this project in your research or academic work, please cite the accompanying paper.

---

## ⭐ If you found this project useful, consider giving it a Star!
