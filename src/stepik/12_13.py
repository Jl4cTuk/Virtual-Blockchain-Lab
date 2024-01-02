import urllib.request
import json
import collections

addr_list = {}

for i in range(450501, 450550):

    url = f"https://blockchain.info/block-height/{i}?format=json"
    print(url)
    r = urllib.request.urlopen(url)
    data = json.load(r)
    b = data['blocks'][0]['tx'][0]['out'][0]['addr']
    if b in addr_list:
        addr_list[b] += 1
    else:
        addr_list.update({b: 1})

c = collections.Counter(addr_list)

print(c.most_common(7))