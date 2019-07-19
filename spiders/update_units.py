import json
from pprint import pprint
# file path: D:\\image\\units.json

with open("D:\\image\\units.json", encoding="utf-8") as file:
    units = json.load(file)

pprint(units[0]['ad data']['تطل على'])
units[0]['ad data']['تطل على'] = 'test'
pprint(units[0]['ad data']['تطل على'])

with open("D:\\image\\units.json",mode='w' ,encoding="utf-8") as file:
    file.write(json.dumps(units))
