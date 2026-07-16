# CleanSlate

CleanSlate is an interactive data cleaning and visualization application built with Streamlit. It simplifies the data preprocessing workflow by allowing users to upload datasets, identify data quality issues, clean the data, generate visualizations, and export the cleaned dataset—all through an intuitive web interface.

The project is designed for students, data analysts, and aspiring data scientists who want a simple yet powerful tool for exploratory data analysis and dataset preprocessing.

---

## Live Demo
https://cleanslate.streamlit.app/

## Features

### Dataset Overview
- Upload CSV datasets
- Preview uploaded data
- View dataset dimensions
- Inspect column names and data types

### Data Quality Report
- Missing value summary
- Duplicate row count
- Memory usage
- Numeric and categorical column counts

### Data Cleaning
- Missing value analysis
- Fill missing values using:
  - Mean
  - Median
  - Mode
  - Ignore
  - Drop Rows
- Remove duplicate rows
- Detect outliers using the IQR method
- Remove detected outliers

### Data Visualization
- Histogram
- Box Plot
- Scatter Plot
- Correlation Heatmap
- Bar Chart
- Pie Chart

### Export
- Download the cleaned dataset as a CSV file


---

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Project Structure

```text
CleanSlate/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── loader.py
│   ├── summary.py
│   ├── quality.py
│   ├── cleaning.py
│   ├── visualization.py
│   └── export.py
│
└── assets/
    └── screenshots/
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/CleanSlate.git
```

### Navigate to the project

```bash
cd CleanSlate
```

### Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Usage

1. Upload a CSV dataset.
2. Review the dataset summary and quality report.
3. Clean missing values using the preferred strategy.
4. Remove duplicate rows.
5. Detect and remove outliers.
6. Generate visualizations to explore the data.
7. Export the cleaned dataset.

---

## Screenshots

### Home

assets/screenshots/image.png

### Dataset Overview

assets/screenshots/image-1.png
assets/screenshots/image-2.png
### Data Cleaning

assets/screenshots/image-3.png
assets/screenshots/image-4.png


### Visualizations
assets/screenshots/image-5.png
assets/screenshots/image-6.png

### Export
assets/screenshots/image-7.png

---

## Future Improvements

- Support Excel (.xlsx) files
- Additional encoding techniques
- Feature scaling options
- Automated cleaning recommendations
- Interactive filtering and sorting
- PDF report generation
- Cloud deployment enhancements

---

## Author

**Nisma**

B.Tech Artificial Intelligence & Data Science

GitHub: https://github.com/<nissmmaaaa>