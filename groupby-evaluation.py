import numpy as np
import os
import json

def compute_accuracy(predictions, ground_truth):
    correct_predictions = 0
    for i in range(len(predictions)):
        predictions[i] = predictions[i].replace('\n', '')
        if predictions[i] == ground_truth[i][0]:
            correct_predictions += 1
    total_samples = len(predictions)
    accuracy = correct_predictions / total_samples
    return accuracy

def compute_precision_at_1(predictions, ground_truth):
    correct_predictions = 0
    if type(predictions) == str:
        for i in range(len(predictions)):
            prediction = predictions[i].replace('\n', '')
            if predictions[i] in set(ground_truth[i]):
                correct_predictions += 1
        total_predictions = len(predictions)
        precision = correct_predictions / total_predictions
        return precision
    else:
        for i in range(len(predictions)):
            if len(predictions[i]) == 0:
                continue
            prediction = predictions[i][0]
            if prediction in set(ground_truth[i]):
                correct_predictions += 1
        total_predictions = len(predictions)
        precision = correct_predictions / total_predictions
        return precision

def compute_ndcg_at_1(predictions, ground_truth):
    if type(predictions) == str:
        dcg = 0
        idcg = 0
        for i in range(len(predictions)):
            predictions[i] = predictions[i].replace('\n', '')
            if predictions[i] in set(ground_truth[i]):
                dcg += 1 / np.log2(2)
            idcg += 1 / np.log2(2)
        ndcg = dcg / idcg
        return ndcg
    else:
        dcg = 0
        idcg = 0
        for i in range(len(predictions)):
            if len(predictions[i]) == 0:
                continue
            prediction = predictions[i][0]
            if prediction in set(ground_truth[i]):
                dcg += 1 / np.log2(2)
            idcg += 1 / np.log2(2)
        ndcg = dcg / idcg
        return ndcg

def compute_ndcg_at_2(predictions, ground_truth):
    if type(predictions) == str:
        return None
    dcg = 0
    idcg = 0
    for i in range(len(predictions)):
        current_predictions = predictions[i]
        for k in range(len(current_predictions)):
            if k >= len(ground_truth[i]):
                continue
            if current_predictions[k] in set(ground_truth[i]):
                dcg += 1 / np.log2(k + 2)
            idcg += 1 / np.log2(k + 2)
    ndcg = dcg / idcg
    return ndcg

predictions = []
ground_truth = []

for subdir, dirs, files in os.walk('./data/groupby_1000'):
    try:
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = json.load(f)
                    predictions.append(content['by'])
            elif file.endswith('.json'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = json.load(f)
                    ground_truth.append(content['by'])
    except Exception as e:
        print(e)
        print("Error reading file.")
        continue

# accuracy = compute_accuracy(predictions, ground_truth)
precision = compute_precision_at_1(predictions, ground_truth)
ndcg_at_1 = compute_ndcg_at_1(predictions, ground_truth)
ndcg_at_2 = compute_ndcg_at_2(predictions, ground_truth)

# print(f'Accuracy: {accuracy:.4f}')
print(f'Precision@1: {precision:.4f}')
print(f'NDCG@1: {ndcg_at_1:.4f}')
print(f'NDCG@2: {ndcg_at_2:.4f}')
