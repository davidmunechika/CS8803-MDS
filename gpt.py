import os
from openai import OpenAI

OPENAI_API_KEY = '{PASTE_OPEN_AI_API_KEY_HERE}'

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=OPENAI_API_KEY,
)

# Specify target operation
operation = 'groupby'

prompt_map = {
  'melt': 'Give me the columns that are reasonable choices to collapse (melt/unpivot) in the csv table below. Simply return the answer, without any other text, as strings in this format: "value_vars": []\n',
  'pivot': 'You will perform a pivot operation on the CSV table below and need to choose the best parameters. Predict which column would be the best index column (left-hand side of the pivot) and which column would be the best header column (columns on top of the result). Simply return the answer, without any text, in this format: {"header": [], "index": []}\n',
  'groupby': 'Tell me the top 2 best columns to groupby in the csv table below. Simply return the column names, without any other text in the format: "by": []\n',
  'join': 'Give me the type of join and a reasonable choice of columns to join these two csv tables below. Simply return the answer, without any other text, as strings in this format: {"how": , "left on": , "right on": }\n'
}

count = 0

# Walk through all directories and subdirectories
for subdir, dirs, files in os.walk('./groupby_1000'):
  # Print progress
  print("PROGRESS: " + str(count) + " / 1000")
  count += 1

  # Skip directories with answer files; we may run this script multiple times on the same directory if we get rate limited
  if any(file.endswith('.txt') for file in files):
    continue
  try:
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".csv"):
            print("Starting file: " + filepath)
            with open(filepath, 'r') as f:
                # Read the first 5 lines of the csv into a string
                data = f.readlines()
                data = data[:10]
                data = ''.join(data)
                print(data)

                # Inject the data into the prompt
                prompt = prompt_map[operation] + data

                # Truncate excessively long prompts to avoid OpenAI API excessive costs
                if len(prompt) > 500:
                  prompt = prompt[:500]

                # Create a completion
                response = client.chat.completions.create(
                  model="gpt-4-1106-preview",
                  messages=[{"role": "system", "content": prompt}],
                  max_tokens=100,
                  temperature=0
                )
                print(response)

                # Extract the response
                answer = response.choices[0].message.content
                print(answer)

                # Write the response to a file in the same directory
                with open(filepath[:-4] + '-answer.txt', 'w') as f:
                    f.write(answer)
  except Exception as e:
    print(e)
    print("Error reading file.")
    continue

print("Done!")

# Deprecated old API usage

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[{"role": "system", "content": "Say this is a test"}],
#   max_tokens=7,
#   temperature=0
# )

# print(response)

# print(response.choices[0].message.content)