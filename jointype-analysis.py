import numpy as np
import os
import json

def compute_metrics(directory):
    precision_count = 0
    total_count = 0
    prediction = None
    ground_truth = None

    for subdir, dirs, files in os.walk(f'./data/{directory}'):
        try:
            for file in files:
                if file.endswith('.txt'):
                    with open(os.path.join(subdir, file), 'r') as f:
                        content = json.load(f)
                        prediction = content['how']
                elif file.endswith('.json'):
                    with open(os.path.join(subdir, file), 'r') as f:
                        content = json.load(f)
                        ground_truth = content['how']
            if prediction == ground_truth:
                precision_count += 1
            total_count += 1
        except Exception as e:
            print(e)
            print("Error reading file.")
            continue
    
    return precision_count / total_count

directories = ["merge_1000_lower", "merge_1000_upper", "merge_1000_lower_column", "merge_1000_upper_column"]

for directory in directories:
    precision = compute_metrics(directory)
    print(f"Precision for {directory}: {precision}")