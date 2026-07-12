import pandas as pd
def load_csv(uploaded_file):
    if uploaded_file is not None:
        """Load a CSV file into a pandas DataFrame."""
        df=pd.read_csv(uploaded_file)
        return df