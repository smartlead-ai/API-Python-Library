# Smartlead API-Python-Library
## Smartlead's Python Library (unofficial)

## Quickstart

```
from smartlead import Smartlead

API_KEY = "your_api_key"

Smartlead.api_key = API_KEY

smartlead = Smartlead()

response = smartlead.v1.campaigns.create("Your campaign", None)

print(response)
```
