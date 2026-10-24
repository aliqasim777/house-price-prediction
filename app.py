import streamlit as st

st.title("House Price Prediction App")

# UI Inputs
area = st.number_input('Area (sq. ft.)', min_value=100, value=205)
bedrooms = st.number_input('Bedrooms', min_value=1, value=1)
bathrooms = st.number_input('Bathrooms', min_value=1, value=1)
parking = st.number_input('Parking spaces', min_value=0, value=1)

location = st.selectbox(
    'Select Location',
    ('Johar Town', 'Bahria Town', 'Gulberg', 'DHA Phase 5')
)

# Prediction button
if st.button('Predict House Price'):
    base_price = (area * 3000) + (bedrooms * 150000) + (bathrooms * 100000) + (parking * 50000)
    
    location_multipliers = {
        'Johar Town': 1.0,
        'Bahria Town': 1.2,
        'Gulberg': 1.5,
        'DHA Phase 5': 2.0
    }
    
    final_price = base_price * location_multipliers[location]
    
    st.success(f"Estimated House Price: Rs. {final_price:,.0f}")
  
    
