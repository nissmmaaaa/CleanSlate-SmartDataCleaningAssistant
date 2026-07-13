import pandas as pd
import streamlit as st


def show_missing_values(df):
    st.subheader("Missing Values Analysis")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        st.success("No missing values found!")
        return

    strategies = {}
    options = ["Ignore", "Mean", "Median", "Mode", "Drop Rows"]

    header1, header2, header3, header4 = st.columns([3, 2, 2, 3])

    with header1:
        st.markdown("**Column**")

    with header2:
        st.markdown("**Missing**")

    with header3:
        st.markdown("**Percentage**")

    with header4:
        st.markdown("**Strategy**")

    st.divider()

    for column in missing.index:

        col1, col2, col3, col4 = st.columns([3, 2, 2, 3])

        with col1:
            st.write(column)

        with col2:
            st.write(f"{missing[column]:,}")

        with col3:
            percentage = (missing[column] / len(df)) * 100
            st.write(f"{percentage:.2f}%")

        with col4:

            if pd.api.types.is_numeric_dtype(df[column]):
                default_strategy = "Median"
            else:
                default_strategy = "Mode"

            strategies[column] = st.selectbox(
                label="Strategy",
                options=options,
                index=options.index(default_strategy),
                key=column,
                label_visibility="collapsed"
            )

    if st.button("Apply Cleaning"):

        cleaned_df = df.copy()
        has_error = False

        for column, strategy in strategies.items():

            if strategy == "Ignore":
                continue

            elif strategy == "Mean":
                if pd.api.types.is_numeric_dtype(cleaned_df[column]):
                    cleaned_df[column] = cleaned_df[column].fillna(
                        cleaned_df[column].mean()
                    )
                else:
                    st.warning(f"⚠️ '{column}' is not numeric. Mean cannot be applied.")
                    has_error = True

            elif strategy == "Median":
                if pd.api.types.is_numeric_dtype(cleaned_df[column]):
                    cleaned_df[column] = cleaned_df[column].fillna(
                        cleaned_df[column].median()
                    )
                else:
                    st.warning(f"⚠️ '{column}' is not numeric. Median cannot be applied.")
                    has_error = True

            elif strategy == "Mode":
                cleaned_df[column] = cleaned_df[column].fillna(
                    cleaned_df[column].mode()[0]
                )

            elif strategy == "Drop Rows":
                cleaned_df = cleaned_df.dropna(subset=[column])

        if not has_error:
            st.session_state.df = cleaned_df
            st.success("Missing values cleaned successfully!")
            st.rerun()