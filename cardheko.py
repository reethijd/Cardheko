import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

# 📌 Load files
try:
    with open('random_forest_final.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Model load error: {e}")

try:
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    st.error(f"Scaler load error: {e}")

try:
    with open('encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)
except Exception as e:
    st.error(f"Encoder load error: {e}")

try:
    with open('model_columns.pkl', 'rb') as f:
        expected_columns = pickle.load(f)
except Exception as e:
    st.error(f"Columns load error: {e}")

# 📌 Load sample data
df = pd.read_excel('cleaned_final_data.xlsx')

st.title("Cardheko✅: Used Car Price Prediction🤖")
st.image("cardheko.gif", use_column_width=True)

# Sidebar Inputs
modelYear = st.sidebar.slider("Model Year", int(df['modelYear'].min()), int(df['modelYear'].max()), 2018)
km = st.sidebar.selectbox("Kilometers Driven", df['km'].unique())
Mileage = st.sidebar.selectbox("Mileage (kmpl)", df['Mileage'].unique())
bt = st.sidebar.selectbox("Body Type", df['bt'].unique())
transmission = st.sidebar.selectbox("Transmission", df['transmission'].unique())
oem = st.sidebar.selectbox("OEM", df['oem'].unique())
model_name = st.sidebar.selectbox("Model", df['model'].unique())
fuel_type = st.sidebar.selectbox("Fuel Type", df['Fuel Type'].unique())
insurance = st.sidebar.selectbox("Insurance Validity", df['Insurance Validity'].unique())
ownership = st.sidebar.selectbox("Ownership", df['Ownership'].unique())
city = st.sidebar.selectbox("City", df['city'].unique())

# Build input DataFrame
user_input = pd.DataFrame([{
    'km': km,
    'modelYear': modelYear,
    'Mileage': Mileage,
    'bt': bt,
    'transmission': transmission,
    'oem': oem,
    'model': model_name,
    'Fuel Type': fuel_type,
    'Insurance Validity': insurance,
    'Ownership': ownership,
    'city': city
}])

num_cols = ['km', 'modelYear', 'Mileage']
cat_cols = ['bt', 'transmission', 'oem', 'model',
            'Fuel Type', 'Insurance Validity', 'Ownership', 'city']

# Scale numerics
scaled_nums = scaler.transform(user_input[num_cols])
scaled_df = pd.DataFrame(scaled_nums, columns=num_cols)

# Encode categoricals
encoded_cats = encoder.transform(user_input[cat_cols])
encoded_cat_cols = encoder.get_feature_names_out(cat_cols)
encoded_df = pd.DataFrame(encoded_cats, columns=encoded_cat_cols)

# Final input with matching columns
final_input = pd.concat([scaled_df, encoded_df], axis=1)
final_input = final_input.reindex(columns=expected_columns, fill_value=0)

# 📌 Format price nicely (lakhs/crores)
def format_price(value):
    if value >= 1e7:
        return f"₹ {value/1e7:.2f} Cr"
    else:
        return f"₹ {value/1e5:.2f} Lakh"

# Predict & show
if st.sidebar.button("Predict Price 💰"):
    prediction = model.predict(final_input)[0]
    formatted_price = format_price(prediction)
    st.success(f"💸 **Estimated Price: {formatted_price}**")
