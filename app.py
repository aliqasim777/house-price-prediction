 import streamlit as st
import streamlit.components.v1 as components

st.title("House Price Prediction App")

area = st.number_input('Area (sq. ft.)', min_value=100, value=205)
bedrooms = st.number_input('Bedrooms', min_value=1, value=1)
bathrooms = st.number_input('Bathrooms', min_value=1, value=1)
stories = st.number_input('Stories / Portions', min_value=1, value=1)
parking = st.number_input('Parking spaces', min_value=0, value=1)

location = st.selectbox(
    'Select Location',
    ('Johar Town', 'Bahria Town', 'Gulberg', 'DHA Phase 5')
)

if st.button('Predict House Price'):
    base_price = (area * 3000) + (bedrooms * 150000) + (bathrooms * 100000) + (stories * 200000) + (parking * 50000)
    
    location_multipliers = {
        'Johar Town': 1.0,
        'Bahria Town': 1.2,
        'Gulberg': 1.5,
        'DHA Phase 5': 2.0
    }
    
    final_price = base_price * location_multipliers[location]
    st.success(f"Estimated House Price: Rs. {final_price:,.0f}")

st.markdown("---")
st.subheader("🏠 Interactive 3D House Model")

house_3d_html = """
<!DOCTYPE html>
<html>
<head>
    <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <style>
        model-viewer {
            width: 100%;
            height: 400px;
            background-color: #f0f2f6;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <model-viewer src="https://modelviewer.dev/shared-assets/models/Astronaut.glb" 
                  alt="A 3D house model" 
                  auto-rotate 
                  camera-controls>
    </model-viewer>
</body>
</html>
"""

components.html(house_3d_html, height=420)
