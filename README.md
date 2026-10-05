# 🏠 House Price Prediction

An AI-powered web application that predicts house prices using a **tuned Random Forest Regression model** trained on the King County house sales dataset.

🌐 **Live Demo:** https://house-price-prediction-7890.streamlit.app/

📂 **GitHub Repository:** https://github.com/vikas7890556/house-price-prediction

---

## 📌 Project Overview

This project uses machine learning to estimate the price of a house based on its characteristics such as:

- Number of bedrooms and bathrooms
- Living area and lot area
- Number of floors
- Waterfront availability
- View and property condition
- Construction grade
- Above-ground and basement area
- Year built
- Location (latitude, longitude, zipcode)
- Average living area of nearby houses

The trained model is integrated into a **Streamlit web application**, allowing users to enter property details and receive an estimated house price instantly.

---

## 🚀 Live Application

Try the deployed application here:

👉 **https://house-price-prediction-7890.streamlit.app/**

Example prediction from the deployed application:

> **Estimated House Price: $319,335.27**

The prediction depends on the property values entered by the user.

---

## 🤖 Machine Learning Model

The final model is a **Random Forest Regressor** with hyperparameter tuning using `GridSearchCV`.

### Final Parameters

```text
n_estimators = 300
max_depth = 20
random_state = 42
```

Categorical preprocessing for `zipcode` is handled using a `ColumnTransformer` and `OneHotEncoder`.

### Model Performance

| Metric | Result |
|---|---:|
| MAE | $72,477.02 |
| RMSE | $146,065.54 |
| R² Score | 85.89% |
| MAPE | 13.11% |

The final trained model is stored as:

```text
house_price_model.pkl
```

The model is tracked using **Git LFS** because of its large file size.

---

## 🧠 Features Used

The model uses the following 16 input features:

```text
bedrooms
bathrooms
sqft_living
sqft_lot
floors
waterfront
view
condition
grade
sqft_above
sqft_basement
yr_built
sqft_living15
lat
long
zipcode
```

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regression
- GridSearchCV
- Joblib

### Web Application
- Streamlit
- Python
- Custom CSS

### Development & Deployment
- VS Code
- Git
- GitHub
- Git LFS
- Streamlit Community Cloud

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── house_price_model.pkl
├── kc_house_data.csv
├── model_training.ipynb
├── streamlit_app.py
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/vikas7890556/house-price-prediction.git
cd house-price-prediction
```

### 2. Create and activate a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```powershell
streamlit run streamlit_app.py
```

---

## 🔄 How It Works

```text
User enters property details
          ↓
Streamlit Web Interface
          ↓
Input data converted to DataFrame
          ↓
Preprocessing pipeline
          ↓
Tuned Random Forest Model
          ↓
Predicted House Price
          ↓
Price displayed to the user
```

---

## 🎯 Project Goals

- Build a practical machine learning regression project
- Improve house price prediction performance
- Use preprocessing for real-world data
- Tune a Random Forest model using GridSearchCV
- Deploy the trained model as an interactive web application
- Provide a simple interface for users

---

## 📊 Example

For one set of property characteristics entered through the application, the deployed model produced:

```text
$319,335.27
```

This value is an ML estimate and should not be considered a professional real-estate valuation.

---

## 👨‍💻 Author

**Vikas Jadhav**

Computer Engineering Student | Machine Learning & Software Projects

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
