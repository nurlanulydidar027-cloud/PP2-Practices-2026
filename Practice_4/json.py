import json

# 1. Dictionary to JSON string (dumps)
user = {"name": "Alice", "age": 25}
json_string = json.dumps(user)
print(json_string)          # {"name": "Alice", "age": 25}

# 2. JSON string to dictionary (loads)
text = '{"name": "Bob", "age": 30}'
user = json.loads(text)
print(user["name"])         # Bob

# 3. Write to file (dump)
data = {"city": "Almaty", "population": 2000000}
with open("city.json", "w") as f:
    json.dump(data, f)

# 4. Read from file (load)
with open("city.json", "r") as f:
    loaded = json.load(f)
print(loaded["city"])       # Almaty

# 5. Pretty print JSON (indent)
person = {"name": "Charlie", "age": 22, "hobbies": ["gaming", "coding"]}
print(json.dumps(person, indent=4))