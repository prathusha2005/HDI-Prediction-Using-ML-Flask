<div align="center">

# Human Development Index (HDI) Prediction Using Machine Learning

A machine learning project for predicting the Human Development Index (HDI) using socio-economic indicators and a trained Linear Regression model.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3%2B-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c?logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13%2B-4C72B0?logo=seaborn&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

> ⭐ Beginner Friendly • Machine Learning • Flask • Portfolio Project

<p align="center">
  <img src="Images/flask_home.png" width="900" alt="HDI Prediction Flask Application">
</p>

</div>

---

# 📚 Table of Contents

- Project Overview
- Features
- Project Workflow
- Technologies Used
- Machine Learning Algorithm
- Dataset Information
- Installation
- How to Run the Flask Application
- Project Highlights
- Project Statistics
- Project Folder Structure
- Sample Prediction
- Screenshots
- Future Improvements
- Learning Outcomes
- Author
- License

---

# 🎯 Project Overview

This project predicts the Human Development Index (HDI) of countries using Machine Learning. It uses socio-economic indicators such as Life Expectancy, Mean Years of Schooling, Expected Years of Schooling, and Gross National Income (GNI) per Capita to estimate the HDI value and classify the country's development level.

---

# ✨ Features

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Correlation heatmap
- Histograms
- Feature importance analysis
- Linear Regression model
- Model comparison
- Flask web application
- HDI prediction
- Responsive user interface
- Input validation
- Model serialization using Joblib

---

# 🔄 Project Workflow

```text
Dataset
↓
Exploratory Data Analysis
↓
Data Preprocessing
↓
Train-Test Split
↓
Model Training
↓
Model Evaluation
↓
Model Comparison
↓
Save Model
↓
Flask Web Application
↓
HDI Prediction
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| Flask | Web Framework |
| HTML | Frontend |
| CSS | Styling |
| Joblib | Model Serialization |

---

# 🤖 Machine Learning Algorithm

This project uses **Linear Regression** to predict HDI values.

The model was compared with other regression algorithms.

| Model | R² Score |
|-------|----------|
| Linear Regression | 0.9892 |
| Decision Tree Regressor | 0.9210 |
| Random Forest Regressor | 0.9719 |

**Best Model:** Linear Regression

---

# 📂 Dataset Information

- Dataset: HDI Dataset
- Number of Records: 124
- Target Variable: HDI

### Input Features

- Country
- Life Expectancy
- Mean Years of Schooling
- Expected Years of Schooling
- GNI per Capita

---

# ⚙ Installation

```bash
git clone https://github.com/prathusha2005/HDI-Prediction-Using-ML-Flask.git

cd HDI-Prediction-Using-ML-Flask

pip install -r requirements.txt
```

---

# 🚀 Run the Flask Application

```bash
cd App

python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

# ✨ Project Highlights

- Machine Learning Project
- Linear Regression Model
- Flask Web Application
- Model Evaluation
- Responsive User Interface
- Input Validation
- GitHub Portfolio Project

---

# 📊 Project Statistics

| Metric | Value |
|---------|-------|
| Dataset Size | 124 Records |
| Number of Features | 5 |
| Target Variable | HDI |
| Best Model | Linear Regression |
| R² Score | 0.9892 |
| Framework | Flask |
| Language | Python |

---

# 📁 Project Folder Structure

```text
HDI-Prediction-Using-ML-Flask

│
├── Dataset/
│      HDI.csv
│
├── Notebook/
│      HDI_Model.ipynb
│
├── Model/
│      HDI_LinearRegression_Model.pkl
│
├── App/
│      app.py
│      templates/
│      static/
│
├── Images/
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

---

# 📈 Sample Prediction

| Input | Value |
|--------|-------|
| Country | India |
| Life Expectancy | 70 |
| Mean Years of Schooling | 7 |
| Expected Years of Schooling | 13 |
| GNI per Capita | 7000 |

**Predicted HDI:** 0.68

**Development Category:** Medium Human Development

---

# 📸 Screenshots

<p align="center">
<img src="Images/correlation_heatmap.png" width="45%">
<img src="Images/model_comparison.png" width="45%">
</p>

<p align="center">
<img src="Images/feature_importance.png" width="45%">
<img src="Images/actual_vs_predicted.png" width="45%">
</p>

<p align="center">
<img src="Images/flask_home.png" width="45%">
<img src="Images/prediction_result.png" width="45%">
</p>

---

# 🚀 Future Improvements

- Deploy on AWS
- Deploy on Azure
- Dockerize the application
- Build a Streamlit version
- Implement XGBoost
- Hyperparameter tuning
- Train with larger datasets
- Develop REST APIs
- Add user authentication

---

# 📚 Learning Outcomes

- Data Cleaning
- Exploratory Data Analysis
- Machine Learning
- Model Evaluation
- Flask Development
- GitHub Project Management

---

# 👨‍💻 Author

**Prathusha**

GitHub: https://github.com/prathusha2005

Repository:

https://github.com/prathusha2005/HDI-Prediction-Using-ML-Flask

---

# 📜 License

This project is intended for educational and learning purposes.