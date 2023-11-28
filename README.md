# Evaluating Zero-Shot Data Preparation Recommendations from Large Language Models
Authors: David Munechika, Meghan Kulkarni, Maansi Jain

## Data Preprocessing
We use the same dataset created in the Auto-Suggest paper for our evaluation.

Data can be downloaded from [this link](https://onedrive.live.com/?authkey=!AGJdHNaO9kJuoLs&id=4EEA81351AF2D84B!7570&cid=4EEA81351AF2D84B). Each instance of an operator invocation is stored under a separate sub-folder with a structure of `[OPERATOR]/[GITREPO]_[FILEPATH]_cell[CELLID]_[OPERATORID]/`. Each sub-folder contains a `data.csv` for the input dataframe fed into the operator (dumped as a csv), and also a `param.json` for the exact parameters used in this invocation (the ground-truth we want to predict).

We randomly sample 1000 subdirectories from each of these operation directories for use in our evaluation.

## Generating Recommendations

### Github Copilot
TODO DESCRIBE STEPS

### GPT
The script `gpt.py` contains all the modularized logic for utilizing the OpenAI API to generate data preperation operation parameter recommendations. In order for this file to work properly, you must add your own OpenAI API key at the top of the file when initializing the client. You can also specify the specific operation you would like to compute parameters for as well as the top-level directory where your data samples for that operation live, and this script will automate the process of generating the recommendations. 

Due to rate limiting and heavy API traffic, it is possible that a particular API call may stall for a few minutes. We recommend using a terminal multiplexer when running this script to allow the session to persist even if the connection is interrupted. 

## Evaluating Results

The evaluation scripts `*-evaluation.py` are individual Python scripts which can be run to compute metrics after all of the the recommendations have been generated. These scripts will print the results of the evaluation to the console.

## Other Scripts

Random sampling of subdirectories for each operation can be done using the `sampling.py` file. This step is highly recommended due to the tremendous size of the full dataset.

If you need to recompute the results for a particular operation, you can delete all existing results files using `cleanup.py`.
