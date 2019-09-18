import json
import urllib.request

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

types = ["street", "amekaji", "dandy", "casual"]

with open('data.json') as json_file:
    json_data = json.load(json_file)

for i in range(len(types)):
    for index, item in enumerate(json_data[types[i]]):
        if urllib.error.HTTPError == 403:
            continue
        else:
            urllib.request.urlretrieve(item, './data/train/' + types[i] +'/'+ str(index)+'.jpg')
        