import streamlit as st
from prediction_helper import predict
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="🎉 Health Insurance Predictor", layout="wide")

st.markdown('<h1 style="text-align:center; font-size:50px; font-weight:bold; color:#4A148C;">🎉 Health Insurance Predictor</h1>', unsafe_allow_html=True)

st.markdown(f"""
    <style>
        .stApp {{
            background: linear-gradient(to right, #E3F2FD, #E1BEE7);
        }}
        label, .stSelectbox label, .stSlider label, .stNumberInput label {{
            color: black;
            font-weight: 600;    
        }}
        .stSlider > div[data-baseweb="slider"] span {{
            color: black !important;
        }}
    </style>
""", unsafe_allow_html=True)

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Married', 'Unmarried'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High Blood Pressure', 'Diabetes & High BP',
        'Thyroid', 'Heart Disease', 'BP & Heart Disease', 'Diabetes & Thyroid',
        'Diabetes & Heart Disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

st.markdown('<h2 style="text-align:center; color:#D81B60;">📋 Enter Your Details</h2>', unsafe_allow_html=True)

age = st.slider('🎂 Age', min_value=18, max_value=100, value=25)
income_lakhs = st.slider('💰 Income in Lakhs', min_value=0, max_value=200, value=10)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox('⚧️ Gender', categorical_options['Gender'])
    smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
    bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])
    employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

with col2:
    number_of_dependants = st.number_input('👨‍👩‍👦 Number of Dependants', min_value=0, step=1, max_value=20)
    marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])
    region = st.selectbox('🌎 Region', categorical_options['Region'])
    genetical_risk = st.slider('🧬 Genetical Risk (0-5)', min_value=0, max_value=5, value=2)

with col3:
    insurance_plan = st.selectbox('📜 Insurance Plan', categorical_options['Insurance Plan'])
    medical_history = st.selectbox('🏥 Medical History', categorical_options['Medical History'])

input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

st.markdown('<h2 style="text-align:center; color:#D81B60;">🔮 Prediction</h2>', unsafe_allow_html=True)

if st.button('🎯 Predict Insurance Cost'):
    prediction = predict(input_dict) * 10

    try:
        formatted_prediction = f"{float(prediction):,.2f} ₹"
    except ValueError:
        formatted_prediction = str(prediction)

    st.markdown(f'''
        <div style="text-align:center; background:linear-gradient(45deg, #4CAF50, #2E7D32); color:white; 
        padding:12px; font-size:20px; font-weight:bold; border-radius:10px; margin-top:20px;">
        💰 Predicted Health Insurance Cost: {formatted_prediction}
        </div>
    ''', unsafe_allow_html=True)
