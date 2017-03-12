import json

print "-----------------  Start script.py --------------- "


data = {}
data['nodes'] = []
data['nodes'].append({
    'id': 'Ignacio',
    'group': 1
})

data['nodes'].append({
    'id': 'Alberto',
    'group': 1
})

data['nodes'].append({
    'id': 'Daniel',
    'group': 1
})


data['links'] = []
data['links'].append({
    'source': 'Ignacio',
    'target': 'Alberto',
    'value': 1
})

data['links'].append({
    'source': 'Ignacio',
    'target': 'Daniel',
    'value': 1
})

data['links'].append({
    'source': 'Daniel',
    'target': 'Alberto',
    'value': 1
})




with open('file.json', 'w') as outfile:
    json.dump(data, outfile)
