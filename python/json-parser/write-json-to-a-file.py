import json

person_dict = {"name": "Bob",
               "languages": ["English", "Fench"],
               "married": True,
               "age": 32
               }

with open('person_write.txt', 'w') as json_file:
    json.dump(person_dict, json_file)
