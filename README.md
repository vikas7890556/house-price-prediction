# 🏠 House Price Prediction

### Machine Learning | Random Forest | Streamlit | Scikit-learn

A machine learning web application that predicts house prices based on property characteristics using a **tuned Random Forest Regression model**.

🚀 **Live Demo:**  
https://house-price-prediction-7890.streamlit.app/

📂 **GitHub Repository:**  
https://github.com/vikas7890556/house-price-prediction

---

## 📌 Overview

This project implements an end-to-end machine learning pipeline for predicting house prices.

The application takes property information such as living area, bedrooms, bathrooms, location, condition, grade, and other characteristics as input and uses a trained Random Forest model to estimate the property's price.

The trained model is integrated into an interactive **Streamlit web application** and deployed using **Streamlit Community Cloud**.

---

## 🚀 Live Application

### Try the application

👉 **https://house-price-prediction-7890.streamlit.app/**

Users can enter property details through the web interface and receive an estimated house price instantly.

### Example

For one set of property characteristics entered into the deployed application:

**Predicted Price: $319,335.27**

> The prediction is a machine learning estimate and should not be considered a professional real-estate valuation.

---

## 🎯 Key Features

- 🏠 House price prediction using Machine Learning
- 🌲 Random Forest Regression
- 🔍 Hyperparameter tuning using GridSearchCV
- ⚙️ Data preprocessing using Scikit-learn
- 📍 Location-based features including latitude, longitude, and zipcode
- 🖥️ Interactive Streamlit interface
- 💾 Trained model saved using Joblib
- ☁️ Deployed on Streamlit Community Cloud
- 📦 Large model file managed using Git LFS

---

## 🤖 Machine Learning Approach

The project follows an end-to-end machine learning workflow:

```text
Dataset
   ↓
Data Preparation
   ↓
Feature Selection
   ↓
Train / Test Split
   ↓
Data Preprocessing
   ↓
Random Forest Regression
   ↓
Hyperparameter Tuning
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Streamlit Application
   ↓
Cloud Deployment
