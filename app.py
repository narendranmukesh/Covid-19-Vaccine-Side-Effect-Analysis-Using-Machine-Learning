import streamlit as st
import numpy as np
import joblib  # Use joblib to load your model

# Load your trained model (replace 'gradient_boost_model.pkl' with your actual model file)
model = joblib.load('random_forest_model.pkl')  # Ensure your model is saved using joblib

# Set up the Streamlit app layout
st.title("COVID-19 Vaccine Side Effects Severity Predictor")

# Collect input data from user
st.write("Please enter the details for prediction:")

# Input fields based on the 4 features the model expects
age = st.number_input("Enter age:", min_value=0, max_value=120, value=90, step=1)
gender = st.selectbox("Gender:", ["Male", "Female"])  # Female = 1, Male = 0
vaccine_type = st.selectbox("Vaccine Type:", ("Pfizer", "Moderna", "Janssen"))  # Three vaccine options
medical_history = st.selectbox("Medical History:", ["Yes", "No"])  # Yes = 1, No = 0

# Map the categorical inputs to numerical format for the model
gender_map = 1 if gender == "Female" else 0  # 1: Female, 0: Male

# Map vaccine type: 0 for Pfizer, 1 for Moderna, 2 for Janssen
vaccine_map = {"Pfizer": 0, "Moderna": 1, "Janssen": 2}[vaccine_type]

medical_history_map = 1 if medical_history == "Yes" else 0  # 1: Medical history exists, 0: No history

# Input data for prediction (4 features)
input_data = np.array([[age, gender_map, vaccine_map, medical_history_map]])

# Make a prediction when the button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 'Severe Side-effects':
        st.error(f"Prediction: {prediction[0]} — The individual is likely to experience severe side effects.")
    else:
        st.success(f"Prediction: {prediction[0]} — The individual is not likely to experience severe side effects.")

# Optionally display the input data for debugging
st.write('Input data:', input_data)