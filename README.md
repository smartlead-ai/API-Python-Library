# Smartlead API-Python-Library
## Smartlead's Python Library (unofficial)
Implementation of Smartlead API in Python. Original API documentation can be found [here](https://help.smartlead.ai/API-Documentation-a0d223bdd3154a77b3735497aad9419f)

## Quickstart
1. Download the GitHub repository
2. Create a folder called "smartlead" in your project's src code directory
3. Extract the `__init__.py` file into your smartlead folder
4. Start using the library!
```
from smartlead import Smartlead

API_KEY = "your_api_key"

Smartlead.api_key = API_KEY

smartlead = Smartlead()

response = smartlead.v1.campaigns.create("Your campaign", None)

print(response)
```
