# Import modul yang akan digunakan
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache()
def load_data():

    # Load dataset
    df = pd.read_csv('gaya_belajar_encoded.csv')

    x = df[["Hobi","Pelajaran_Suka","Metode_belajar"]]
    y = df["Rekomendasi"]

    return df, x, y

@st.cache()
def train_model(x, y):
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )

    model.fit(x, y)

    score = model.score(x, y)

    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)

    # Ensure features is a 1D list or array, then reshape for prediction
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    
    return prediction, score


