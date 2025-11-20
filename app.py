import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction App")
st.markdown("Upload your model and predict car prices easily!")

# Load model
model = joblib.load("car_price_prediction_model.pkl")

# UI Inputs
brand = st.selectbox("Brand", ["Toyota","Ford","BMW","Audi","Tesla","Honda","Mercedes"])
model_name = st.text_input("Model")
fuel = st.selectbox("Fuel Type", ["Petrol","Diesel","Electric","CNG"])
trans = st.selectbox("Transmission", ["Manual","Automatic"])
condition = st.selectbox("Condition", ["New","Like New","Used"])
mileage = st.number_input("Mileage", min_value=0)
engine = st.number_input("Engine Size (L)", min_value=0.0, format="%.2f")
age = st.number_input("Age (Years)", min_value=0)

# Predict Button
if st.button("Predict Price"):
    data = pd.DataFrame([{
        "Brand": brand,
        "Model": model_name,
        "Fuel Type": fuel,
        "Transmission": trans,
        "Condition": condition,
        "Mileage": mileage,
        "Engine Size": engine,
        "Age": age
    }])

    prediction = model.predict(data)[0]

    st.success(f"Predicted Price: ₹ {prediction:,.2f}")
