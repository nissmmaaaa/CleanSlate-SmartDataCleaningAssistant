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

import seaborn as sns


def show_correlation_heatmap(df):

    st.subheader("Correlation Heatmap")

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        st.info("At least two numeric columns are required.")
        return

    correlation = numeric_df.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )

    st.pyplot(fig)
def show_boxplot(df):

    st.subheader("Box Plot")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if not numeric_columns:
        st.info("No numeric columns available.")
        return

    column = st.selectbox(
        "Select a numeric column",
        numeric_columns,
        key="boxplot"
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.boxplot(df[column].dropna())

    ax.set_title(f"Box Plot of {column}")
    ax.set_ylabel(column)

    st.pyplot(fig)
def show_scatter_plot(df):

    st.subheader("Scatter Plot")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_columns) < 2:
        st.info("At least two numeric columns are required.")
        return

    col1, col2 = st.columns(2)

    with col1:
        x_column = st.selectbox(
            "X-axis",
            numeric_columns,
            key="scatter_x"
        )

    with col2:
        y_column = st.selectbox(
            "Y-axis",
            numeric_columns,
            index=1,
            key="scatter_y"
        )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(df[x_column], df[y_column])

    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f"{y_column} vs {x_column}")

    st.pyplot(fig)
def show_bar_chart(df):

    st.subheader("Bar Chart")

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if not categorical_columns:
        st.info("No categorical columns available.")
        return

    column = st.selectbox(
        "Select a categorical column",
        categorical_columns,
        key="bar_chart"
    )

    counts = df[column].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(counts.index.astype(str), counts.values)

    ax.set_title(f"Top 10 Categories in {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    plt.xticks(rotation=45)

    st.pyplot(fig)
def show_pie_chart(df):

    st.subheader("Pie Chart")

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if not categorical_columns:
        st.info("No categorical columns available.")
        return

    column = st.selectbox(
        "Select a categorical column",
        categorical_columns,
        key="pie_chart"
    )

    counts = df[column].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        counts.values,
        labels=counts.index.astype(str),
        autopct="%1.1f%%"
    )

    ax.set_title(f"{column} Distribution")

    st.pyplot(fig)