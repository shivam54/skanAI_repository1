import json
import datetime
import os
# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# List contents of the directory
print(f"Contents of the directory: {os.listdir()}")

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Print current working directory after change
print(f"Current working directory after change: {os.getcwd()}")

# Get the absolute path of the response.json file
response_file_path = os.path.join(os.getcwd(), 'response.json')
print(f"Absolute path of response.json: {response_file_path}")

# Read JSON from file
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
