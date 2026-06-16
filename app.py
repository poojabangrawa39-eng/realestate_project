import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_model.pkl")

st.set_page_config(page_title="House Price Prediction")
st.title("🏠 House Price Prediction")

st.write("Enter house details:")

bhk = st.selectbox("Flat Type / BHK", [1, 2, 3, 4, 5])

rooms = st.number_input(
    "Number of Rooms",
    min_value=1,
    max_value=20,
    value=5,
    step=1
)

house_age = st.number_input(
    "House Age (Years)",
    min_value=0,
    max_value=100,
    value=5,
    step=1
)

population = st.number_input(
    "Area Population",
    min_value=1000,
    value=30000,
    step=1000
)

# Fixed average income value
income = 60000

if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "Avg. Area Income": [income],
        "Avg. Area House Age": [house_age],
        "Avg. Area Number of Rooms": [rooms],
        "Avg. Area Number of Bedrooms": [bhk],
        "Area Population": [population]
    })

    price = model.predict(input_data)[0]

    st.success(f"🏡 Predicted House Price: ₹ {price:,.2f}")