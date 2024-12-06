import requests
import json
import sys

x = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=topu")

o = x.json()
for result in o["results"]:
    print(result["trackName"])