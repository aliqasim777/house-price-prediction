import streamlit as st

st.title("House Price Prediction App")

# UI Inputs
area = st.number_input('Area (sq. ft.)', min_value=100, value=205)
bedrooms = st.number_input('Bedrooms', min_value=1, value=1)
bathrooms = st.number_input('Bathrooms', min_value=1, value=1)
# Yahan max_value=5 add kar diya hai taake 3 ya us se zyada stories select ki ja saken
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

# --- Dynamic House Image Section based on Stories ---
st.markdown("---")
st.subheader("🏠 House Design Preview")

# Ab yahan 1, 2 aur 3 (ya us se zyada) teeno ke liye alag images aayengi
if stories == 1:
    st.image("https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=800&q=80", 
             caption="Single Story House Design", use_column_width=True)
elif stories == 2:
    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80", 
             caption="Double Story Luxury House Design", use_column_width=True)
else:
    st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80", 
             caption=f"3-Story / Multi-Portion Modern Villa ({stories} Stories)", use_column_width=True)
