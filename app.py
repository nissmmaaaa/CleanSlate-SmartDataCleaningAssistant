import streamlit as st
from utils.summary import show_summary

from utils.loader import load_csv
st.set_page_config(page_title="CleanSlate", page_icon="🧹", layout="wide")
st.title("CleanSlate")
st.subheader("Transform your data effortlessly with CleanSlate! 🧹")
st.write("Upload a CSV file to clean, analyze, and visualize your dataset in seconds.")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])  
if uploaded_file is not None:
    df=load_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.subheader("Dataset Preview:")
    st.dataframe(df.head(10),use_container_width=True)
    st.caption("Showing first 10 rows of the dataset.")
    show_summary(df)