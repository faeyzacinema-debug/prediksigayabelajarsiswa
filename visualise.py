import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn import tree
from sklearn.tree import export_graphviz
import streamlit as st

from web_function import train_model

def app(df, x, y):

    warnings.filterwarnings("ignore")

    st.title("Visualisasi Prediksi Gaya Belajar")
    # Train the model once and reuse it
    model, score = train_model(x, y)

    if st.checkbox("Plot Confusion Matrix"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ConfusionMatrixDisplay.from_estimator(model, x, y, display_labels=['Auditori', 'Visual','Kinesthetic'], cmap=plt.cm.Blues, values_format='d', ax=ax)
        st.pyplot(fig)

    if st.checkbox("Plot Decision Tree"):
        dot_data = export_graphviz(
        decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
        feature_names=x.columns, class_names=['Auditori', 'Visual','Kinesthetic']
        )

        st.graphviz_chart(dot_data)