import requests
from pyht import Client

client = Client(  
   user_id="75pOT2tsO5RTEwISw8bzMnbMj9b2",  
   api_key="a68681928c1f4a329a1aefed810b481e",  
)

url = "https://api.play.ht/api/v2/voices"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)