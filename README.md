# 📱 Mobile Usage Addiction Prediction

## 📌 Project Overview

The **Mobile Usage Addiction Prediction** project is a Machine Learning application that predicts mobile usage addiction levels based on users' behavioral and lifestyle factors.

The project uses Python and Machine Learning algorithms to preprocess the data, select important features, train different regression models, and evaluate their performance.

## 🎯 Objective

The main objective of this project is to analyze users' mobile usage patterns and predict their mobile usage addiction level using Machine Learning techniques.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Seaborn

## 📊 Dataset

The dataset contains user-related behavioral and lifestyle information such as:

* Age
* Gender
* Daily Usage Hours
* Social Media Usage
* Gaming Time
* Sleep Hours
* Anxiety Level
* Depression Level
* Phone Checks
* Screen Time Before Bed

## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Exploratory Data Analysis
5. Feature Selection
6. Model Training
7. Model Evaluation
8. Streamlit Deployment

## 🔍 Feature Selection

**SelectKBest** with `f_regression` was used to select the most important features for the regression model.

## 🤖 Machine Learning Algorithms

The following regression algorithms were implemented:

* Linear Regression
* K-Nearest Neighbors (KNN) Regression
* Decision Tree Regression
* Random Forest Regression
* Gradient Boosting Regression

## 📈 Model Evaluation

The models were evaluated using:

* **MAE (Mean Absolute Error)** – measures the average absolute difference between actual and predicted values.
* **MSE (Mean Squared Error)** – gives more penalty to larger errors.
* **RMSE (Root Mean Squared Error)** – measures prediction error in the same unit as the target.
* **R² Score** – measures how well the model explains the variation in the target variable.

## 🚀 Streamlit Application

The trained Machine Learning model was integrated with **Streamlit** to create an interactive web application.

Users can enter the required information and receive a predicted mobile usage addiction level.

## 📁 Project Structure

```text
Mobile_Usage_Addiction/
│
├── app.py
├── model_pipe_mobile.pkl
├── requirements.txt
├── README.md
└── dataset/
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project folder

```bash
cd Mobile_Usage_Addiction
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## 💡 Key Learning

Through this project, I gained practical experience in:

* Data preprocessing
* Exploratory Data Analysis
* Feature selection
* Regression algorithms
* Model evaluation
* Machine Learning pipeline creation
* Streamlit deployment

## 👩‍💻 Author

**Shaik Saida Banu**

B.Tech Computer Science Engineering (AI)
