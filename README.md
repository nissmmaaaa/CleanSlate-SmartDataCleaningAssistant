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

<img width="1471" height="660" alt="image" src="https://github.com/user-attachments/assets/b83bca36-6921-4878-994b-843bf81bde15" />


### Dataset Overview
<img width="1474" height="618" alt="image" src="https://github.com/user-attachments/assets/9727b755-0520-48f5-8959-4fa60df47a7a" />
<img width="1490" height="625" alt="image" src="https://github.com/user-attachments/assets/af47121a-77a0-4874-bae9-6f9abf2928e4" />

### Data Cleaning
<img width="1481" height="559" alt="image" src="https://github.com/user-attachments/assets/32d1eddc-7172-4603-a428-80133aa52fdd" />
<img width="1459" height="468" alt="image" src="https://github.com/user-attachments/assets/4532ca42-a306-4250-8215-5e19730f6cb1" />



### Visualizations
<img width="1475" height="696" alt="image" src="https://github.com/user-attachments/assets/44d03ab5-ba50-4ead-abdb-265ad01638c4" />
<img width="1455" height="682" alt="image" src="https://github.com/user-attachments/assets/9e18fc24-8cb4-40f7-a30b-d9e18c8fc41e" />


### Export
<img width="1504" height="685" alt="image" src="https://github.com/user-attachments/assets/b5228b3a-d657-42fe-857c-543b7687fbee" />

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

GitHub: https://github.com/nissmmaaaa
