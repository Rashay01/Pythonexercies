#tuple vs list
#tuple - immutable | list - mutable

person = ("Alex", "SA", 20)
print(person, type(person))

print(person.count(20)) #Finds occurance
print(person.index(20))# Finds the index of the element

#index throw error if not found 
