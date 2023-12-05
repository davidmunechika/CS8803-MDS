import os
import json

def compute_metrics(directory):
    correct_count = 0
    total_count = 0
    header = None
    index = None
    ground_truth_header = None
    ground_truth_index = None

    for subdir, dirs, files in os.walk(f'./data/{directory}'):
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

    return correct_count / total_count

directories = ["pivot_1000_lower", "pivot_1000_upper", "pivot_1000_lower_column", "pivot_1000_upper_column"]

# for directory in directories:
#     accuracy = compute_metrics(directory)
#     print(f"Accuracy for {directory}: {accuracy}")

accuracy = compute_metrics("pivot_1000")
print(f"Accuracy for pivot_1000: {accuracy}")