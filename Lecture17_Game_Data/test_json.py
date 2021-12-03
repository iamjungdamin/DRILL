import json

numbers = [1,2,3,4]
numbers_str = json.dumps(numbers)
print(numbers_str)

value_string = '{"x":10, "y":10}'   # str
values = json.loads(value_string)
print(values)                       # dict
