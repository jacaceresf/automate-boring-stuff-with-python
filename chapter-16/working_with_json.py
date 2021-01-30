import json
import pprint

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

# it will convert the json data to a python format
jsonData = json.loads(stringOfJsonData)

print(f'Before load => {stringOfJsonData}')
print(f'After load => {jsonData}')

for k, v in jsonData.items():
    print(f'Key [{k}] Value [{v}]')

# using the dumps (dump string) we can translate a Pyhton value into a JSON string
pythonValue = {
    'title': 'The Empire strickes back',
    'year': 1980,
    'winOscar': False,
    'saga': 'Skywalker',
    'director': None,
    'actors': ['Mark Hammill', 'Harrison Ford'],
    'actress': ['Carrie Fisher']
}

#we can specify the indent parameter and sort_keys
strJson = json.dumps(pythonValue, indent=4, sort_keys=True)
print(strJson)
