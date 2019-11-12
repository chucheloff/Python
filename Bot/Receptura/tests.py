import json


with open('userbase.json', 'r') as f:
    json_data = json.load(f)

print(json_data)