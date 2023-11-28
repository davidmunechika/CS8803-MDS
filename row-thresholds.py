import os
import shutil
import pandas as pd

source_directory = "./data/merge_1000"
lower_destination_directory = f"{source_directory}_lower"
upper_destination_directory = f"{source_directory}_upper"

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    num_rows = len(df)
    return num_rows

row_lengths = []

for subdir, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            num_rows = analyze_csv(file_path)
            row_lengths.append(num_rows)

top_25_percentile = pd.Series(row_lengths).quantile(0.75)
bottom_25_percentile = pd.Series(row_lengths).quantile(0.25)

for subdir, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(subdir, file)
            num_rows = analyze_csv(file_path)
            if num_rows < bottom_25_percentile:
                destination_subdir = os.path.join(lower_destination_directory, os.path.relpath(subdir, source_directory))
                shutil.copytree(subdir, destination_subdir)
                break
            elif num_rows > top_25_percentile:
                destination_subdir = os.path.join(upper_destination_directory, os.path.relpath(subdir, source_directory))
                shutil.copytree(subdir, destination_subdir)
                break

print(f"Copied subdirectories with table length less than {bottom_25_percentile} to {lower_destination_directory}.")
print(f"Copied subdirectories with table length greater than {top_25_percentile} to {upper_destination_directory}.")
