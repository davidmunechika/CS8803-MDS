import os
import shutil
import pandas as pd

source_directory = "./data/merge_1000"
lower_destination_directory = f"{source_directory}_lower_column"
upper_destination_directory = f"{source_directory}_upper_column"

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    num_cols = len(df.columns)
    return num_cols

col_lengths = []

for subdir, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            num_cols = analyze_csv(file_path)
            col_lengths.append(num_cols)

top_25_percentile = pd.Series(col_lengths).quantile(0.75)
bottom_25_percentile = pd.Series(col_lengths).quantile(0.25)

for subdir, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            num_cols = analyze_csv(file_path)
            if num_cols < bottom_25_percentile:
                destination_subdir = os.path.join(lower_destination_directory, os.path.relpath(subdir, source_directory))
                shutil.copytree(subdir, destination_subdir)
                break
            elif num_cols > top_25_percentile:
                destination_subdir = os.path.join(upper_destination_directory, os.path.relpath(subdir, source_directory))
                shutil.copytree(subdir, destination_subdir)
                break

print(f"Copied subdirectories with table column length less than {bottom_25_percentile} to {lower_destination_directory}.")
print(f"Copied subdirectories with table length greater than {top_25_percentile} to {upper_destination_directory}.")
