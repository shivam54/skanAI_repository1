import json
import datetime

# Read JSON from file
with open('response.json', 'r') as file:
    data = json.load(file)

# Manipulate data
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data['title'] = f'Updated Title - {timestamp} shivamData'

# Save manipulated data back to file
with open('manipulatedResponse.json', 'w') as file:
    json.dump(data, file, indent=2)

# Print manipulated data
print(f'Manipulated JSON Response: {json.dumps(data, indent=2)}')
