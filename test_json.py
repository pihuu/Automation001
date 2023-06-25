import json
data = '{"k1":"val1","k2":"val2"}'
json_result = json.loads(data)
print(json_result['k1'])
print(json_result.get('k1'))
