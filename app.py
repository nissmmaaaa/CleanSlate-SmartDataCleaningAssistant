import streamlit as st
from utils.summary import show_summary
from utils.quality import show_quality_report
from utils.cleaning import show_missing_values
from utils.cleaning import show_duplicate_removal
from utils.cleaning import show_outlier_detection

from utils.loader import load_csv
st.set_page_config(page_title="CleanSlate", page_icon="🧹", layout="wide")
st.sidebar.title("CleanSlate")
st.sidebar.markdown("---")
st.sidebar.header("Navigation")
st.sidebar.write("Overview ")
st.sidebar.write("Cleaning")
st.sidebar.write("Visualizations")
st.sidebar.write("Export")
st.title("CleanSlate")
st.subheader("Transform your data effortlessly with CleanSlate! ")
st.markdown("---")
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])  
if uploaded_file is not None:
    if "df" not in st.session_state:
        st.session_state.df = load_csv(uploaded_file)

    df = st.session_state.df
    st.success("File uploaded successfully!")
    st.subheader("Dataset Preview:")
    st.dataframe(df.head(10),use_container_width=True)
    st.caption(
    f"Showing first 10 of {len(df):,} rows."
)
    show_summary(df)
    show_quality_report(df)
    show_missing_values(df)
    show_duplicate_removal(df)
    show_outlier_detection(df)