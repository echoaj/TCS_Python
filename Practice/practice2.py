
import json

# import json and read allergies.json
with open('allergies.json', 'r') as json_file:
    allergy_types = json.load(json_file)

print(allergy_types)
