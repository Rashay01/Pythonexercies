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

print()
print()
#===========================================================================================
outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}

#--------------------------------------------Task 1-------------------------------------
# Task 1
# Which are outdoor_gadgets ? 
# {'Smartwatch',  'Drone'}
print("Task 1")
new_outdoor_gadgets = set()
for key, value in activity_gadgets.items():
  if value in outdoor_activities:
    new_outdoor_gadgets.add(key)
print(new_outdoor_gadgets)

#or

new_outdoor_activities1 = {key for key, value in activity_gadgets.items() 
  if  value in outdoor_activities}

print(new_outdoor_activities1)

#or

new_outdoor_gadgets2 = set([key for key, value in activity_gadgets.items() 
                              if  value in outdoor_activities])

print(new_outdoor_gadgets2)

#--------------------------------------------Task 2-------------------------------------
# Task 2
# # Which are indoor_gadgets ?
print("Task 2")
new_indoor_gadgets = set()
for key, value in activity_gadgets.items():
  if value in indoor_activities:
    new_indoor_gadgets.add(key)

print(new_indoor_gadgets)


#--------------------------------------------Task 3-------------------------------------
# Task 3
print("Task 3")
def get_activity_gadgets(activity_gadgets, activity_list):
  return set([gadget for gadget, activity in activity_gadgets.items() 
              if activity in activity_list])


print(get_activity_gadgets(activity_gadgets,outdoor_activities))
print(get_activity_gadgets(activity_gadgets,indoor_activities))


#or

def get_activity_gadgets1(activity_gadgets, activity_list):
  return {gadget for gadget, activity in activity_gadgets.items() 
              if activity in activity_list}

print(get_activity_gadgets1(activity_gadgets,outdoor_activities))
print(get_activity_gadgets1(activity_gadgets,indoor_activities))