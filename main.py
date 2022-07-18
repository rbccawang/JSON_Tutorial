'''
JSON (JavaScript Object Notation) is a data representation format
Supports:
- Strings
- Numbers
- Booleans
- Null
- Arrays
- Objects {“key”:”value”}
'''

import json

companies_string = '''
{
"companies": [
  {
    "name": "Deep Sea Mining",
    "numOfEmployees": 100,
    "ceo": ["BG", "GS"],
    "has_license": false,
    "rating": 3.5
  },
  {
    "name": "ISA",
    "numOfEmployees": 5,
    "ceo": null,
    "has_license": true,
    "rating": 1
  }
]
}
'''

data = json.loads(companies_string)

print(data)
print(type(data)) # dictionary

for company in data['companies']:
  print(company["name"])
  del company['rating']

new_string = json.dumps(data, indent = 2, sort_keys = True) # easy to read, alphabetal is sort_keys
print(new_string)