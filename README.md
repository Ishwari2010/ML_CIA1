# 🔐 Intrusion Detection System using XGBoost and LSTM

## 📌 Project Overview
This project implements an **Intrusion Detection System (IDS)** using Machine Learning and Deep Learning techniques to detect malicious network activity. The system analyzes network traffic data and classifies it as **Normal** or **Attack** using the NSL-KDD dataset.

The project implements and compares two models:

- **XGBoost (Ensemble Machine Learning Model)**
- **LSTM (Deep Learning Model)**

A **Streamlit-based web interface** is developed to demonstrate real-time prediction.

---

## 🎯 Objectives
- Detect cyber attacks using machine learning techniques.
- Compare performance of XGBoost and LSTM models.
- Evaluate model performance using classification metrics.
- Provide a user-friendly interface for intrusion detection.

---

## 📊 Dataset
- **Dataset Used:** NSL-KDD Dataset
- Contains network traffic features such as:
  - Protocol type
  - Service
  - Flag
  - Connection statistics
- Target label:
  - `0 → Normal`
  - `1 → Attack`

---

## ⚙️ Implementation Steps

### 1. Data Preprocessing
- Load NSL-KDD dataset
- Convert labels into binary format
- Encode categorical features
- Normalize feature values

### 2. Feature Selection and Data Splitting
- Separate input features and target label
- Split dataset into training and testing sets

### 3. Model Training
- Train XGBoost classifier
- Train LSTM deep learning model

### 4. Model Evaluation
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

### 5. Model Deployment
- Save trained model using Joblib
- Develop Streamlit UI for prediction

---

## 🤖 Models Used

### 🔹 XGBoost
- Ensemble learning technique
- Combines multiple decision trees
- High accuracy and fast performance

### 🔹 LSTM
- Deep learning neural network
- Captures time-based patterns
- Detects complex attack behavior

---

## 📈 Performance Metrics
The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

XGBoost achieved high classification accuracy and efficient detection performance.

---

## 🖥️ Streamlit Interface
The project includes a web interface that allows users to:

- Upload network traffic data
- Perform preprocessing automatically
- Detect intrusion activity
- Display prediction results

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- XGBoost
- TensorFlow / Keras
- Pandas
- NumPy
- Matplotlib / Seaborn
- Streamlit

---

## 🚀 How to Run the Project

### Install Dependencies
```bash
pip install pandas numpy scikit-learn xgboost tensorflow streamlit

python -m streamlit run app.py