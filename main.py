#import library yang dibutuhkan

import streamlit as st
from web_function import load_data


from Tabs import home, predict, visualise

Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise
}

# membuat sidebar
st.sidebar.title("Menu")

# membuat radio option
page = st.sidebar.radio("pages", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#kondisi call app function
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app(df)