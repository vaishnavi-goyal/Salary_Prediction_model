
import streamlit as st

st.title(" Salary Prediction App")

name = st.text_input("Enter Job Title")

experience = st.number_input("Experience", 0, 40, 1)

if st.button("Predict"):
    salary = 50000 + (experience * 5000)
    st.success(f"Predicted Salary: ${salary}")