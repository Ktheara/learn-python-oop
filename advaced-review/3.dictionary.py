# A dictionary is a collection which is unordered, changeable and indexed. A dictionary consists of a collection of key-value pairs.
#https://www.python-engineer.com/courses/advancedpython/03-dict/

# create dictionary
dict_1 = {"name":"Theara", "age": 25, "city":"Phnom Penh"}
print(dict_1)
 
# create dictionary using dict constructor
dict_2 = dict(name="Theara", age=27, city="Phnom Penh")
print(dict_2)

# Access items
name_dict_2 = dict_2["name"]
print(name_dict_2)

# Add new key to dictionary
dict_2["email"] = "theara729@gmail.com"
print(dict_2)

# Delete key form dictionary
del dict_2["email"]
print(dict_2)

# Return value and remove key
print("Popped name: ", dict_2.pop("age"))

# Return and remove the last key-value
print("Popitem: ", dict_2.popitem())
print(dict_2)

# Clear all pairs
dict_2.clear()

# Check for keys
dict_3 = dict(name="Dara", age=34, city="Kampot", job="Electrical")

if "name" in dict_3:
    print(dict_3["name"])

try:
    print(dict_3["firstname"])
except KeyError:
    print("Firstname Not Found.")

# Looping
print("looping: ")
for key in dict_3:
    print(key, dict_3[key])

for key in dict_3.keys():
    print(key)

for value in dict_3.values():
    print(value)

for key, value in dict_3.items():
    print(key, value)

# Merge tow dictionary
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)
