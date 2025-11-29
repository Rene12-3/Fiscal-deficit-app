import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load the trained model
model = joblib.load("fiscal_deficit_model.joblib")

st.title("📊 Fiscal Deficit-to-GDP Prediction Model")
st.write("Enter fiscal indicators to forecast next year's deficit-to-GDP ratio.")

# -------------------------------
# User Input Fields (Match Model Features)
# -------------------------------
country = st.text_input("Country", "Kenya")
debt_to_gdp = st.number_input("Debt-to-GDP Ratio (%)", value=55.0)
deficit_lag1 = st.number_input("Previous Year Deficit-to-GDP (%)", value=3.0)
revenue_to_gdp = st.number_input("Revenue-to-GDP Ratio (%)", value=20.0)
expenditure_to_gdp = st.number_input("Expenditure-to-GDP Ratio (%)", value=25.0)

# Convert input to DataFrame in the correct order
input_data = pd.DataFrame({
    'debt_to_gdp': [debt_to_gdp],
    'deficit_lag1': [deficit_lag1],
    'revenue_to_gdp': [revenue_to_gdp],
    'expenditure_to_gdp': [expenditure_to_gdp]
})

# -------------------------------
# Predict Button
# -------------------------------
if st.button("🔮 Predict Deficit-to-GDP"):
    prediction = model.predict(input_data)[0]
    st.success(f"📉 Predicted Deficit-to-GDP Ratio for {country}: **{prediction:.2f}%**")

    # Simple Visualization
    fig = px.bar(
        x=["Predicted Deficit"],
        y=[prediction],
        labels={"x": "Metric", "y": "Value (%)"},
        title=f"Fiscal Deficit Forecast for {country}"
    )
    st.plotly_chart(fig)

st.caption("Developed by Rene for 10Alytics Hackathon 🚀")
