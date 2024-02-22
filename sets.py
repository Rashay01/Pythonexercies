#String, List, Tuble, Dictonary, Set
#Sets - Like List Mutable but only uniquie

# {}

tech_gadgets = {'Smaartphone', 'Laptop','Smartwatch', 'Tablet', 'Tablet'}
tech_gadgets_list = ['Smaartphone', 'Laptop','Smartwatch', 'Tablet', 'Tablet']

print(tech_gadgets)
print(tech_gadgets_list)

tech_gadgets.add("E-reader") #order doesnt matter
print(tech_gadgets)


more_gadgets = ['Drone', 'Selfiestick']
tech_gadgets.update(more_gadgets) #cant add dictonary
print(tech_gadgets)

# .remove -> error | .discard ->safer
tech_gadgets = {'Smartphone', "Laptop", "Smartwatch", "Tablet", "Tablet"}
#tech_gadgets.remove("Table") #Key error when you dont have correct key
print(tech_gadgets)
tech_gadgets.discard("Tablet")


empty_set= set() # empty set 


outdoor_activities = {'Hicking', 'Cycling', 'Swimming'}
indoor_activties = {'Gaming', 'Reading', 'Cycling'}

print()
#operations on a set
print(outdoor_activities.intersection(indoor_activties)) # return a set 
print(outdoor_activities.union(indoor_activties)) # return a set with cycling once
print(outdoor_activities.difference(indoor_activties)) # return a set
print(indoor_activties.difference(outdoor_activities))
# returns alll the items not common
print(outdoor_activities.symmetric_difference(indoor_activties))

#convertlist to set 
colors = ["red", "blue", "red", "green", "pink", "blue"]

#Long method
ans3 = set()
for color in colors:
  ans3.add(color)

#Easy method/hard
ans = set()
ans.update(colors)
print(ans)

#short method
ans2 = set(colors)
print(ans2, list(ans2))

