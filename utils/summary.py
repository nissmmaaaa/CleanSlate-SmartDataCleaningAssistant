import streamlit as st
import pandas as pd

def show_summary(df):
    """Display a summary of the DataFrame."""
    st.subheader("Dataset Overview:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rows", df.shape[0])
        
    with col2:
        st.metric("Columns", df.shape[1])
    column_df = pd.DataFrame({
    "Column Name": df.columns
})

    st.dataframe(column_df, use_container_width=True)
    st.write("### Data Types")
    st.dataframe(
        df.dtypes.reset_index().rename(
            columns={
                "index" : "Column",
                0 : "Data Type"
            }
        ),
        use_container_width=True
    )
    