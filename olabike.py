import streamlit as st
import pandas as pd
import pickle
import bz2
import joblib
import datetime

# Load the trained model
def load_model():
    # Use full absolute path to the .pbz2 file
    with bz2.BZ2File(bikeriderequest.pbz2", 'rb') as f:
        model = pickle.load(f)
    return model


# Call the function to load the model
model = load_model()


# Title for the Streamlit app
st.title("DgeniusBike Ride Prediction App")


# Display a brief description
st.write("""
This app allows you to predict the number of bike rentals based on various factors such as temperature, humidity, and time of day.
""")

# Step 1: Input data (simulate user input with widgets)
st.header("Enter ride details")

season = st.selectbox("Season", [1, 2, 3, 4])  # 1: Spring, 2: Summer, 3: Fall, 4: Winter
temp = st.slider("Temperature", -10.0, 40.0, 20.0)
humidity = st.slider("Humidity (%)", 0, 100, 50)
windspeed = st.slider("Windspeed", 0.0, 60.0, 10.0)
date = st.date_input("Date")
hour = st.slider("Hour", 0, 23, 12)

# Build additional features
dt = datetime.datetime.combine(date, datetime.time(hour))
month = dt.month
day_of_week = dt.weekday()
holiday = 0  # You can add logic to determine if it's a holiday
atemp = temp - 2  # Just an example adjustment

# Example of making a prediction (you can adjust the feature names as needed)
if st.button("Predict"):
    # Placeholder logic - you can improve this with real conditions
    weather = 1  # For example, 1 = Clear, 2 = Mist, etc.
    workingday = 1 if dt.weekday() < 5 else 0  # Weekday = working day, weekend = not

    # Create a DataFrame with the user input
    input_data = pd.DataFrame([[
        season, holiday, workingday, weather, temp,
        atemp, humidity, windspeed, hour, day_of_week, month
    ]], columns=[
        'season', 'holiday', 'workingday', 'weather', 'temp',
        'atemp', 'humidity', 'windspeed', 'hour', 'day_of_week', 'month'
    ])

# Use the loaded model to make a prediction
    prediction = model.predict(input_data)

    # Round the prediction to the nearest integer
    rounded_prediction = round(prediction[0])

    # Display the rounded predicted result
    st.write(f"Predicted bike rentals: {rounded_prediction}")
