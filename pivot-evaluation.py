import os
import json

correct_count = 0
total_count = 0

for subdir, dirs, files in os.walk('pivot_1000'):
    try:
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = json.load(f)
                    if len(content["header"]) == 0:
                        header = set()
                    else:
                        header = set(content["header"])
                    if len(content["index"]) == 0:
                        index = set()
                    else:
                        index = set(content["index"])
            elif file.endswith('.json'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = json.load(f)
                    if len(content["column"]) == 0:
                        ground_truth_header = set()
                    else:
                        ground_truth_header = set(content["column"])
                    if len(content["index"]) == 0:
                        ground_truth_index = set()
                    else:
                        ground_truth_index = set(content["index"])
        if len(header.intersection(ground_truth_header)) > 0 or len(index.intersection(ground_truth_index)) > 0:
            correct_count += 1
        total_count += 1
                
    except Exception as e:
        print(e)
        print("Error reading file.")
        print(subdir)
        continue

print("Accuracy: ", correct_count / total_count)