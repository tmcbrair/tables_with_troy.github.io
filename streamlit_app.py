import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from joblib import load

# Load the trained model
loaded_model = load('trained_model.joblib')

def predict_home_value(county_value, sales_price, fin_sqft, total_bathrooms):
    # Calculate value discrepancy and size efficiency
    value_discrepancy = sales_price - county_value
    size_efficiency = sales_price / fin_sqft

    # Create input array based on the order of features in your model
    input_data = [fin_sqft, total_bathrooms, value_discrepancy, size_efficiency]  # Adjust this based on your model's input features

    # Predict the home's final value
    predicted_value = loaded_model.predict([input_data])
    
    return f"The predicted home value is: ${predicted_value[0]:,.2f}"

# Streamlit interface
st.title('Home Value Prediction')

# Input components
county_value = st.number_input('County Value', value=100000.0)
sales_price = st.number_input('Sales Price', value=120000.0)
fin_sqft = st.number_input('Square Footage (Finished)', value=1500.0)
total_bathrooms = st.number_input('Total Bathrooms', value=2.0)

# Button to trigger prediction
if st.button('Predict Home Value'):
    result = predict_home_value(county_value, sales_price, fin_sqft, total_bathrooms)
    st.write(result)