import numpy as np
import os
import json

precision_count = 0
total_count = 0

for subdir, dirs, files in os.walk('merge_1000'):
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

print("Precision: ", precision_count / total_count)
