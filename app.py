import streamlit as st

st.title("House Price Prediction App")

# UI Inputs
area = st.number_input('Area (sq. ft.)', min_value=100, value=205)
bedrooms = st.number_input('Bedrooms', min_value=1, value=1)
bathrooms = st.number_input('Bathrooms', min_value=1, value=1)
stories = st.number_input('Stories / Portions', min_value=1, max_value=5, value=1)
parking = st.number_input('Parking spaces', min_value=0, value=1)

location = st.selectbox(
    'Select Location',
    ('Johar Town', 'Bahria Town', 'Gulberg', 'DHA Phase 5')
)

# Prediction button
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

# --- House Image Section (Same 3D Image for all stories with dynamic caption) ---
st.markdown("---")
st.subheader("🏠 House Design Preview")

# Aapki di gayi 3D image ka link
house_image_url = "https://media.istockphoto.com/id/2217479261/photo/3d-rendering-of-two-story-house-with-concrete-facade-in-night.jpg?s=612x612&w=0&k=20&c=51Mvu3T3TDl4qLpWpqbUt_jBENVS6oh03I9eMjY0nJE="

if stories == 1:
    st.image(house_image_url, caption="1-Story House (3D Design)", use_column_width=True)
elif stories == 2:
    st.image(house_image_url, caption="2-Story House (3D Design)", use_column_width=True)
else:
    st.image(house_image_url, caption=f"{stories}-Story House (3D Design)", use_column_width=True)
