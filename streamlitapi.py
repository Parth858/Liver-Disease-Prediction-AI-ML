import streamlit as st
import numpy as np
import pickle

# Load the scaler and model
scaler = pickle.load(open('C:/Users/kulkarpa/Desktop/assignments ExcelR/Project/scaler.pkl', 'rb'))
model = pickle.load(open('C:/Users/kulkarpa/Desktop/assignments ExcelR/Project/svm_liver_disease_model.pkl', 'rb'))

# Title and Description
st.title("Liver Disease Prediction")
st.write("""
This app predicts the likelihood of liver disease based on user-provided health parameters.
""")

# User Inputs
def user_input():
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex", ("Male", "Female"))
    albumin = st.number_input("Albumin", value=3.5, format="%.2f")
    alkaline_phosphatase = st.number_input("Alkaline Phosphatase", value=100, format="%.0f")
    alanine_aminotransferase = st.number_input("Alanine Aminotransferase", value=50, format="%.0f")
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", value=50, format="%.0f")
    bilirubin = st.number_input("Bilirubin", value=1.0, format="%.2f")
    cholinesterase = st.number_input("Cholinesterase", value=7.0, format="%.2f")
    cholesterol = st.number_input("Cholesterol", value=200.0, format="%.2f")
    creatinina = st.number_input("Creatinina", value=1.0, format="%.2f")
    gamma_glutamyl_transferase = st.number_input("Gamma-Glutamyl Transferase", value=30.0, format="%.0f")
    protein = st.number_input("Protein", value=6.5, format="%.2f")

    # Gender Encoding
    sex_encoded = 1 if sex == "Male" else 0

    # Arrange the input array in the exact order of the training features
    data = np.array([[age, sex_encoded, albumin, alkaline_phosphatase, alanine_aminotransferase,
                      aspartate_aminotransferase, bilirubin, cholinesterase, cholesterol,
                      creatinina, gamma_glutamyl_transferase, protein]])
    return data

# Collect input
input_data = user_input()

# Scale input data
scaled_data = scaler.transform(input_data)

# Predict and Display
if st.button("Predict"):
    prediction = model.predict(scaled_data)
    if prediction[0] == 1:
        st.write("The patient is likely to have liver disease.")
    else:
        st.write("The patient is unlikely to have liver disease.")
