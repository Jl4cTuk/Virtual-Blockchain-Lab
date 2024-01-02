import urllib.request
import json

count = 0

for i in range(0, 15):
    url = f"https://blockchain.info/block-height/{i}?format=json"
    r = urllib.request.urlopen(url)
    data = json.load(r)
    sp = data['blocks'][0]['tx'][0]['out'][0]['spent']
    if sp == False:
        count += 1

print (15 - count)