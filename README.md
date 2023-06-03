# Smartlead API-Python-Library
## Smartlead's Python Library (unofficial)
Implementation of Smartlead API in Python. Original API documentation can be found [here](https://help.smartlead.ai/API-Documentation-a0d223bdd3154a77b3735497aad9419f)

## Quickstart

```
from smartlead import Smartlead

API_KEY = "your_api_key"

Smartlead.api_key = API_KEY

smartlead = Smartlead()

response = smartlead.v1.campaigns.create("Your campaign", None)

print(response)
```
