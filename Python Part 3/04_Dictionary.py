my_dictionary= {
    
    "jamil" : "math",
    "josim" : "math",
    "jahid" : "eng",
    "jhon" : "geo"
}

print(type(my_dictionary))
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

print(my_dictionary["jamil"])

new_item = {"bob": "Bio"}
print(my_dictionary.update(new_item))
print(my_dictionary)

for key, value in my_dictionary.items():
    print(key, value)