import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Mobile Usage Addiction",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Mobile Usage Addiction")
st.write("Enter the user's details below.")

# Load model
with open("model_pipe_mobile.pkl","rb") as file:
    model = pickle.load(file)

# -----------------------------
# USER INPUTS
# -----------------------------

Sleep_Hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

Time_on_Social_Media = st.number_input(
    "Time on Social Media (hours)",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

Time_on_Gaming = st.number_input(
    "Time on Gaming (hours)",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

Anxiety_Level = st.number_input(
    "Anxiety Level",
    min_value=0,
    max_value=10,
    value=5
)

Time_on_Education = st.number_input(
    "Time on Education (hours)",
    min_value=0.0,
    max_value=24.0,
    value=2.0
)

Depression_Level = st.number_input(
    "Depression Level",
    min_value=0,
    max_value=10,
    value=5
)

Exercise_Hours = st.number_input(
    "Exercise Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

Interllectual_Performance = st.number_input(
    "Intellectual Performance",
    min_value=0,
    max_value=100,
    value=70
)

Self_Esteem = st.number_input(
    "Self Esteem",
    min_value=0,
    max_value=10,
    value=5
)

Phone_Checks_Per_Day = st.number_input(
    "Phone Checks Per Day",
    min_value=0,
    max_value=500,
    value=50
)

Social_Interactions = st.number_input(
    "Social Interactions",
    min_value=0,
    max_value=100,
    value=5
)

Phone_Usage_Purpose = st.selectbox(
    "Phone Usage Purpose",
    ["Social Media", "Gaming", "Education", "Entertainment", "Other"]
)

Weekend_Usage_Hours = st.number_input(
    "Weekend Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

Family_Communication = st.number_input(
    "Family Communication",
    min_value=0,
    max_value=100,
    value=5
)

Screen_Time_Before_Bed = st.number_input(
    "Screen Time Before Bed (hours)",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

Apps_Used_Daily = st.number_input(
    "Apps Used Daily",
    min_value=0,
    max_value=200,
    value=20
)

Daily_Usage_Hours = st.number_input(
    "Daily Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)


Age = st.number_input(
    "Age",
    min_value=5,
    max_value=100,
    value=20
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


# -----------------------------
# CREATE DATAFRAME
# -----------------------------

input_data = pd.DataFrame({
    "Age": [Age],
    "Gender": [Gender],
    "Daily_Usage_Hours": [Daily_Usage_Hours],

    "Sleep_Hours": [Sleep_Hours],
    "Time_on_Social_Media": [Time_on_Social_Media],
    "Time_on_Gaming": [Time_on_Gaming],
    "Anxiety_Level": [Anxiety_Level],
    "Time_on_Education": [Time_on_Education],
    "Depression_Level": [Depression_Level],
    "Exercise_Hours": [Exercise_Hours],
    "Interllectual_Performance": [Interllectual_Performance],
    "Self_Esteem": [Self_Esteem],
    "Phone_Checks_Per_Day": [Phone_Checks_Per_Day],
    "Social_Interactions": [Social_Interactions],
    "Phone_Usage_Purpose": [Phone_Usage_Purpose],
    "Weekend_Usage_Hours": [Weekend_Usage_Hours],
    "Family_Communication": [Family_Communication],
    "Screen_Time_Before_Bed": [Screen_Time_Before_Bed],
    "Apps_Used_Daily": [Apps_Used_Daily]
})

# -----------------------------
# PREDICTION
# -----------------------------

if st.button("🔮 Predict Mobile Addiction"):

    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")

    st.subheader("Input Data")
    st.dataframe(input_data)