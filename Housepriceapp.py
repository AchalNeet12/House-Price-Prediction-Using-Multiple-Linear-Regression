import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import base64

# Function to set background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}"); 
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: White; /* Set text color to White for better visibility */
    }}
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
        color: Black; /* Ensure headers are also Black */
    }}
    .sidebar .sidebar-content {{
        background-color: rgba(0, 0, 0, 0.5); /* Dark background for sidebar */
        color: White; /* White text on the sidebar */
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set background (make sure to provide the correct image path)
set_background("Background.jpg!d")

# Load the dataset
dataset = pd.read_csv(r"E:\3.spyder\Regression\linear regression\Multiple linear regressin\House_data.csv")

# Prepare the data
X = dataset.iloc[:, [3, 4, 5, 7, 9, 14]]  # Selected features
y = dataset.iloc[:, 2]  # Dependent variable (price)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header('📈 Input Features')

# Get user inputs with corresponding feature names
feature1 = st.sidebar.number_input('🔑 Bedrooms (Feature 1): Number of bedrooms', min_value=0, value=0)
feature2 = st.sidebar.number_input('🔑 Bathrooms (Feature 2): Number of bathrooms', min_value=0, value=0)
feature3 = st.sidebar.number_input('🔑 Square Footage (Feature 3): Sqft of living space', min_value=0, value=0)
feature4 = st.sidebar.number_input('🔑 View Quality (Feature 4): View quality (0-4)', min_value=0, max_value=4, value=0)
feature5 = st.sidebar.number_input('🔑 Year Built (Feature 5): Year of construction', min_value=1900, value=2000)
feature6 = st.sidebar.number_input('🔑 Living Area (Feature 6): Sqft of living area in 15 closest neighbors', min_value=0, value=0)

# Add some spacing to the sidebar
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)

# Create the predict button
predict_button = st.sidebar.button('Predict House Price')

# Streamlit frontend
st.title('🏡 House Price Prediction')

# Prediction logic when button is clicked
if predict_button:
    # Prepare input data
    user_input = np.array([feature1, feature2, feature3, feature4, feature5, feature6]).reshape(1, -1)
    
    # Predict the house price using the model
    predicted_price = regressor.predict(user_input)

    # Display the result
    st.markdown(f"###### 📊 Predicted House Price: **${predicted_price[0]:,.2f}**")
    st.markdown("<br><br>", unsafe_allow_html=True)

st.write("---")
st.write("This app demonstrates a Multiple linear regression model for HousePrice prediction.")