import requests
import json
from models.body_quicktype import *

# Get API's response
response = requests.get('https://api.le-systeme-solaire.net/rest.php/bodies')

# Base code
values = response.json()
elements = values['bodies']
for dict_body in elements:
    print(dict_body)

# # Quicktype code
# result = video_from_dict(json.loads(response.text))
# print(result)
