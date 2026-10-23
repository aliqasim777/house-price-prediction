import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter house details to estimate its price.")

# App ke andar hi model train karne ka function taaki koi error na aaye
@st.cache_resource
def get_trained_model():
    data = {
        'area': [1500, 2500, 3000, 3500, 4000, 1200, 2200, 2800, 3200, 4500],
        'bedrooms': [2, 3, 3, 4, 4, 1, 2, 3, 4, 5],
        'bathrooms': [1, 2, 2, 3, 3, 1, 1, 2, 3, 4],
        'stories': [1, 2, 2, 2, 3, 1, 1, 2, 2, 3],
        'parking': [1, 2, 1, 2, 3, 0, 1, 1, 2, 2],
        'price': [3000000, 5000000, 5500000, 7000000, 8500000, 2500000, 4000000, 5200000, 6800000, 9500000]
    }
    df = pd.DataFrame(data)
    X = df[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
    y = df['price']
    
    model = LinearRegression()
    model.fit(X, y)
    return model

model = get_trained_model()

with st.form("house_prediction_form"):
    area = st.number_input("Area (sq. ft.)", min_value=100, value=3000)
    bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
    stories = st.number_input("Stories", min_value=1, value=2)
    parking = st.number_input("Parking spaces", min_value=0, value=1)
    
    submit = st.form_submit_button("Predict House Price")

if submit:
    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking
    }])
    
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated House Price: Rs. {prediction:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

