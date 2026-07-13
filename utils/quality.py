import streamlit as st
def show_quality_report(df):
    st.subheader("Data Quality Report")
    total_missing = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    memory_usage = df.memory_usage(deep=True).sum() / (1024 ** 2) 
    numeric_columns = df.select_dtypes(include=['number']).shape[1]
    categorical_columns = df.select_dtypes(include=['object', 'category']).shape[1]
    col1,col2,col3,col4,col5=st.columns(5)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        with st.container(border=True):
            st.metric("Missing Values", total_missing)

    with col2:
        with st.container(border=True):
            st.metric("Duplicate Rows", duplicate_rows)

    with col3:
        with st.container(border=True):
            st.metric("Memory Usage", f"{memory_usage:.2f} MB")

    with col4:
        with st.container(border=True):
            st.metric("Numeric Columns", numeric_columns)

    with col5:
        with st.container(border=True):
            st.metric("Categorical Columns", categorical_columns)