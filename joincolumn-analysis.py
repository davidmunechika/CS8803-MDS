import numpy as np
import os
import json

def compute_metrics(directory):
    precision_count = 0
    dcg_count = 0
    idcg_count = 0
    total_count = 0
    ground_truth = None
    predictions = None

    for subdir, dirs, files in os.walk(f'./data/{directory}'):
        try:
            for file in files:
                if file.endswith('.txt'):
                    with open(os.path.join(subdir, file), 'r') as f:
                        content = json.load(f)
                        predictions = content["left on"]
                elif file.endswith('.json'):
                    with open(os.path.join(subdir, file), 'r') as f:
                        content = json.load(f)
                        ground_truth = content["left on"]
            if type(ground_truth) == list:
                if predictions in set(ground_truth):
                    precision_count += 1
                    dcg_count += 1 / np.log2(2)
                idcg_count += 1 / np.log2(2)
                total_count += 1
            else:
                if predictions == ground_truth:
                    precision_count += 1
                    dcg_count += 1 / np.log2(2)
                idcg_count += 1 / np.log2(2)
                total_count += 1
                    
        except Exception as e:
            print(e)
            print("Continuing...")
            continue
    
    return precision_count / total_count, dcg_count / idcg_count

directories = ["merge_1000_lower", "merge_1000_upper", "merge_1000_lower_column", "merge_1000_upper_column"]

for directory in directories:
    precision, ndcg = compute_metrics(directory)
    print(f"Precision@1 for {directory}: {precision}")
    print(f"NDCG@1 for {directory}: {ndcg}")

