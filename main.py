import json
import os

# Define the folder containing JSON files
folder_path = 'json'

# Iterate through each JSON file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            
        if 'name' in data:
            data['name'] = data['name'].replace(' ', '')
        
        # Remove the "compiler" field if it exists
        if 'compiler' in data:
            del data['compiler']
        
        # Set the "attributes" array to be empty
        data['attributes'] = []
        
        # Write the cleaned JSON back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
