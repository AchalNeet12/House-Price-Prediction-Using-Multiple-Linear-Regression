# **House Price Prediction**
---

## Overview
**This project is a House Price Prediction App built using Streamlit and Multiple Linear Regression.** It predicts house prices based on various features such as the number of bedrooms, bathrooms, square footage, year built, and other important factors. The app offers a user-friendly interface where users can input property details to estimate its price.

---

## Multiple Linear Regression
Multiple Linear Regression is a statistical technique used to model the relationship between one dependent variable (y) and two or more independent variables (𝑋1,𝑋2,...,𝑋𝑛)

Equation:

           y=b0 + b1X1 + b2X2 +...+bnX n
Where:

- y: Dependent variable (predicted value, e.g., house price).
- 𝑏0: Intercept.
- 𝑏1,𝑏2,...,𝑏𝑛: Coefficients for independent variables.
- 𝑋1,𝑋2,...,𝑋𝑛: Independent variables.

 # Role of Multiple Linear Regression in the Project
1. **Purpose:** To model the relationship between house prices and multiple influencing factors.
2. **Feature Weights:** Determines the impact of each feature (e.g., square footage, year built) on the house price.
3. **Prediction:** Generates house price estimates based on the user’s input.
4. **Interpretability:** Offers insights into which features are most important in determining house prices.
   
By incorporating multiple features, the regression model provides more accurate and robust predictions compared to simple linear regression, which only uses a single independent variable.

---
​
## Dataset
1. **Source:** The dataset (House_data.csv) contains data about houses, including features and their corresponding prices.
2. **Features Used:**
 - **Number of bedrooms:** Total bedrooms in the house.
 - **Number of bathrooms:** Total bathrooms in the house.
 - **Square footage of living area:** Total square footage.
 - **View quality:** A numerical rating of the house's view (0-4).
 - **Year built:** Year the house was constructed.
 - **Living area of 15 closest neighbors:** Average square footage of living areas in the neighborhood.
3. **Target Variable:**
 - **House price:** The price of the house, used as the dependent variable.

---

## Data Preprocessing Steps
- **Data Loading:**
Load the dataset from a CSV file.
- **Feature Selection:**
Select relevant columns from the dataset that significantly impact the house price.
- **Handling Missing Data:**
Ensure no null or missing values in the dataset before training the model.
- **Splitting Data:**
Split the data into training (80%) and testing (20%) sets using train_test_split.
- **Model Training:**
Train a Multiple Linear Regression model using the training set.

---

## Features
1. **User Input:**
Inputs for key house features like bedrooms, bathrooms, square footage, view quality, year built, and living area.
2. **Prediction:**
Estimates the house price using a pre-trained Multiple Linear Regression model.
3. **Interactive Interface:**
A visually appealing and easy-to-use interface with input forms and prediction display.
4. **Customization:**
Styled layout with a background image and sidebar for user inputs.

---

## Technology Used
1. **Programming Language:**
 - Python
2. **Framework:**
 - Streamlit: For building the interactive web app.
3. Libraries:
 - NumPy: For numerical computations.
 - Pandas: For data manipulation.
 - Scikit-learn: For building and evaluating the regression model.
 - Base64: For encoding the background image.

---

## Results
The model predicts house prices based on user-provided inputs for the selected features.

---

## Conclusion
The project effectively demonstrates the use of Multiple Linear Regression to predict house prices. The app provides a simple, yet powerful interface for users to interact with the model. While the predictions depend on the quality and relevance of the data, this project lays the foundation for more advanced models and datasets.


