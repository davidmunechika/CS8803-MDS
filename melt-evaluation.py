import os
import json

accuracy_count = 0
total_count = 0
average_precision = 0
average_recall = 0

for subdir, dirs, files in os.walk('./melt_1000'):
    answer = set()
    ground_truth = set()
    try:
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(subdir, file), 'r') as f:
                    content = f.read()
                    start_index = content.find('[')
                    end_index = content.find(']')
                    if start_index != -1 and end_index != -1:
                        variables_list = content[start_index + 1:end_index]
                        variables = [var.strip(' " ') for var in variables_list.split(',')]
                        answer = set(variables)
            elif file.endswith('.json'):
                with open(os.path.join(subdir, file), 'r') as f:
                    ground_truth = set(json.load(f)['value_vars'])
        
        if len(answer) == 0 or len(ground_truth) == 0:
            continue

        if answer == ground_truth:
            accuracy_count += 1
        total_count += 1

        true_positives = len(answer.intersection(ground_truth))
        false_positives = len(answer.difference(ground_truth))
        false_negatives = len(ground_truth.difference(answer))
        if true_positives + false_positives == 0:
            precision = 0
        else:
            precision = true_positives / (true_positives + false_positives)
        if true_positives + false_negatives == 0:
            recall = 0
        else:
            recall = true_positives / (true_positives + false_negatives)

        average_precision += precision
        average_recall += recall
    except Exception as e:
        print(e)
        print("Error reading file.")
        continue

accuracy = accuracy_count / total_count
average_precision = average_precision / total_count
average_recall = average_recall / total_count
f1_score = 2 * average_precision * average_recall / (average_precision + average_recall)

print('Accuracy: ', accuracy)
print('Average Precision: ', average_precision)
print('Average Recall: ', average_recall)
print('F1 Score: ', f1_score)