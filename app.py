import streamlit as st
from utils.summary import show_summary
from utils.quality import show_quality_report
from utils.cleaning import show_missing_values
from utils.cleaning import show_duplicate_removal
from utils.cleaning import show_outlier_detection
from utils.visualizations import (
    
    show_histogram,
    show_correlation_heatmap,
    show_boxplot,
    show_bar_chart,
    show_pie_chart,
    show_scatter_plot


)
from utils.export import export_data

from utils.loader import load_csv
st.set_page_config(page_title="CleanSlate", page_icon="🧹", layout="wide")




st.title("CleanSlate")
st.subheader("Transform your data effortlessly with CleanSlate! ")
st.markdown("---")
page = st.pills(
    "",
    [
        "Overview",
        "Cleaning",
        "Visualizations",
        "Export"
    ],
    default="Overview",
    label_visibility="collapsed"
)
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv","xlsx"])  
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
    if page == "Overview":

        show_summary(df)
        show_quality_report(df)

    elif page == "Cleaning":

        show_missing_values(df)
        show_duplicate_removal(df)
        show_outlier_detection(df)

    elif page == "Visualizations":

        show_histogram(df)
        show_boxplot(df)
        show_scatter_plot(df)
        show_correlation_heatmap(df)
        show_bar_chart(df)
        show_pie_chart(df)

    elif page == "⬇Export":

        export_data(df, uploaded_file.name)