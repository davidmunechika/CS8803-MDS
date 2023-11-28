import os
import shutil
import random

# Source directory where you want to select subdirectories from
source_directory = './groupby_data_csv'

# Destination directory where you want to copy the selected subdirectories
destination_directory = './groupby_10000'

# Number of subdirectories to select
num_subdirectories_to_select = 10000

# List all subdirectories in the source directory
subdirectories = [os.path.join(source_directory, d) for d in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, d))]

# Ensure that we don't try to select more subdirectories than available
if num_subdirectories_to_select > len(subdirectories):
    num_subdirectories_to_select = len(subdirectories)

# Randomly select num_subdirectories_to_select subdirectories
selected_subdirectories = random.sample(subdirectories, num_subdirectories_to_select)

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Copy the selected subdirectories to the destination directory
for subdirectory in selected_subdirectories:
    shutil.copytree(subdirectory, os.path.join(destination_directory, os.path.basename(subdirectory)))

print(f"{num_subdirectories_to_select} subdirectories copied to {destination_directory}")
