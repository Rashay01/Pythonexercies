#HaspMap -> Key: Value
# keys should be unique

# [] -> List
# () -> Tuple
# {} -> Dict

# person = {
#   "name" : " Siya Kolisi",
#   "age" : 32,
#   "country" : "South Africa",
#   "sport" : "Rugy"
# }

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

# for key, value in person.items():
#   print(key, value)

#

# #Safty for value
# print(person.get("height"))

# #Safty for value with default value
# #get("Key", default_value)
# print(person.get("height", 175))

# person = {
#   "name" : " Siya Kolisi",
#   "age" : 32,
#   "address" : {
#     "city" : "Port Elizabeth",
#   "country" : "South Africa",
#   },
#   "height" : 186,
#   "sport" : "Rugby"
# }

# print(person["address"].get("city"))
# print(person["address"]["city"])

#print(person.get("stats").get("city")) #AttributeError NoneType

#print(person.get("stats",{}).get("city"))

#dictonary comprehension
nums = {x: x**2 for x in range(10)}
print(nums)

nums = {x: x**2 for x in range(10) if x % 2 == 0}
print(nums)