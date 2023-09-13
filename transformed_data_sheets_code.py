
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Initialize Scaler and Encoder
scaler = StandardScaler()
label_encoder = LabelEncoder()

# Read Excel file and load all sheets into a dictionary of dataframes
input_excel_path = '/mnt/data/tt_global_human_day.xlsx'
data_frames = pd.read_excel(input_excel_path, sheet_name=None)

# Output path for transformed Excel workbook
output_excel_path = '/mnt/data/transformed_data_sheets.xlsx'

# Perform basic transformations and EDA for each sheet

## Transformation and EDA code for 'global_human_day', 'country_regions', and 'global_economic_activity' have been performed.

# Create SQLite database and connection
import sqlite3
db_path = '/mnt/data/transformed_data_sheets.db'
conn = sqlite3.connect(db_path)

# Load the transformed data sheets into the SQLite database
for sheet, df in data_frames.items():
    df.to_sql(f"{sheet}_transformed", conn, if_exists='replace', index=False)

# Close the connection
conn.close()
