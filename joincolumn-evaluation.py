import numpy as np
import os
import json

precision_count = 0
dcg_count = 0
idcg_count = 0
total_count = 0

for subdir, dirs, files in os.walk('./data/merge_1000'):
    try:
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = json.load(f)
                    predictions = content["right on"]
            elif file.endswith('.json'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = json.load(f)
                    ground_truth = content["right on"]
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

print("Precision@1: ", precision_count / total_count)
print("NDCG@1: ", dcg_count / idcg_count)

