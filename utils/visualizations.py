import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def show_histogram(df):

    st.write("#### Histogram")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if not numeric_columns:
        st.info("No numeric columns available.")
        return

    column = st.selectbox(
        "Select a numeric column",
        numeric_columns,
        key="histogram"
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.hist(df[column].dropna(), bins=20, color='black', edgecolor='white')

    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    st.pyplot(fig)