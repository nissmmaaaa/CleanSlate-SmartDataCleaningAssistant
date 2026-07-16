import streamlit as st


def export_data(df):

    st.subheader("⬇ Export Cleaned Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Cleaned CSV",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )