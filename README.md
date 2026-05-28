# 🎓 Student Performance Predictor

## 📌 Overview

This project predicts student academic performance based on demographic, socio-economic, and study-related factors. The dataset includes attributes such as **gender, race/ethnicity, parental education level, lunch type, test preparation course**, and scores in **math, reading, and writing**.

The goal is to build machine learning models that can help educators and researchers identify patterns in student achievement and predict outcomes effectively.

---

## 📂 Dataset

The dataset (`stud.csv`) contains the following columns:

- **gender** – Male/Female
- **race_ethnicity** – Student group (A–E)
- **parental_level_of_education** – Highest education level of parents
- **lunch** – Standard or free/reduced lunch
- **test_preparation_course** – Completed or none
- **math_score, reading_score, writing_score** – Exam scores

Example row:

---

## ⚙️ Features

- 🔍 **Data Preprocessing**: Handling missing values, encoding categorical features
- 📊 **Exploratory Data Analysis (EDA)**: Visualizations using Seaborn & Matplotlib
- 🤖 **Machine Learning Models**: Regression & classification approaches (Linear Regression, Random Forest, XGBoost)
- 📈 **Model Evaluation**: Metrics like RMSE, MAE, Accuracy, and R²
- 🖥️ **Streamlit Web App**: Interactive interface for predictions

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/username/student-performance-predictor.git
cd student-performance-predictor

pip install -r requirements.txt

streamlit run app.py
```
