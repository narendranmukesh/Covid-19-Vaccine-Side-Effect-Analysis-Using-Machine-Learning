# Covid-19-Vaccine-Side-Effect-Analysis-Using-Machine-Learning
ML-based model to predict the severity of COVID-19 vaccine side effects using VAERS data. Includes data preprocessing, class balancing (SMOTE), and models like Random Forest to classify reports as severe or non-severe, aiding in vaccine safety analysis.

🦠 COVID-19 Vaccine Side Effect Predictor
This project uses machine learning to predict the severity of COVID-19 vaccine side effects using real-world data from the VAERS (Vaccine Adverse Event Reporting System) database.

📌 Project Overview
The goal is to classify vaccine reaction reports into:

Severe Side Effects

No Severity

This helps in analyzing vaccine safety and supporting public health decision-making.

🧾 Datasets Used
VAERS_DATA.csv

VAERS_VAX.csv

VAERS_SYMPTOM.csv

Year: 2021

Source: VAERS Official Site

⚙️ Techniques Used

Data Preprocessing and Cleaning

Feature Selection and Encoding

Handling Imbalanced Data:

OverSampling

SMOTE

Model Building:

Random Forest

Logistic Regression

Ensemble Models

Performance Evaluation:

Accuracy, Precision, Recall, F1-score, ROC Curve

📈 Results
The Random Forest model gave the best results with balanced class performance and a good ROC-AUC score after applying SMOTE
