import json
import datetime
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Read JSON from file
response_file_path = os.path.join(script_directory, 'response.json')
with open(response_file_path, 'r') as file:
    data = json.load(file)

# Manipulate data
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data['title'] = f'Updated Title - {timestamp} shivamData'

# Save manipulated data back to file
manipulated_response_file_path = os.path.join(script_directory, 'manipulatedResponse.json')
with open(manipulated_response_file_path, 'w') as file:
    json.dump(data, file, indent=2)

# Print manipulated data
print(f'Manipulated JSON Response: {json.dumps(data, indent=2)}')
