
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter house details to estimate its price.")

MODEL_PATH = Path(__file__).parent / "house_price_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

if not MODEL_PATH.exists():
    st.error("house_price_model.pkl file is missing!")
    st.stop()

model = load_model()

with st.form("house_prediction_form"):
    area = st.number_input("Area (sq. ft.)", min_value=100, value=3000)
    bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
    stories = st.number_input("Stories", min_value=1, value=2)
    parking = st.number_input("Parking spaces", min_value=0, value=1)

    mainroad = st.selectbox("Main road access", ["yes", "no"])
    guestroom = st.selectbox("Guest room", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwaterheating = st.selectbox("Hot water heating", ["yes", "no"])
    airconditioning = st.selectbox("Air conditioning", ["yes", "no"])
    prefarea = st.selectbox("Preferred area", ["yes", "no"])

    furnishingstatus = st.selectbox(
        "Furnishing status",
        ["furnished", "semi-furnished", "unfurnished"]
    )

    submit = st.form_submit_button("Predict House Price")

if submit:
    house = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }])

    try:
        prediction = model.predict(house)[0]
        st.success(f"Estimated House Price: {prediction:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.warning(
            "Input columns must match the model training columns."
        )
