#HaspMap -> Key: Value
# keys should be unique

# [] -> List
# () -> Tuple
# {} -> Dict

person = {
  "name" : " Siya Kolisi",
  "age" : 32,
  "country" : "South Africa",
  "sport" : "Rugy"
}

# #access a value
# print(person)
# print(person["name"])

# #update
# person["age"] += 1 
# print(person)

#Methods
#Iteable -> List, Tuple, dict_keys 
# print(person.keys())
# print(person.values())
# print(person.items())

for key, value in person.items():
  print(key, value)