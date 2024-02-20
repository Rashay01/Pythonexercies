marks =[98, 75, 40, 45, 80, 60]
marks.pop()
#marks.pop(3) #removes at index 3
print(marks[:-3])
print(marks)

marks.remove(40)
print(marks)
marks.append(67)
print(marks)
marks.insert(2,77)
print(marks)
print([5,2] *2)
ans= [5,2]
ans2 = [4,7]
print(ans +ans2)


ans3 = ans2 #creates a another pointer to the memory address 
#ans3.pop()
print(ans2)

#stores the first item memory adddress 

ans4 = ans2[:] #creates a copy of the list
ans2.pop()
print(ans4,ans2)
ans5 = ans4.copy() #creates a copy of the list
ans4.pop()
print(ans4,ans5)
print(id(ans4),id(ans5)) #shows mwmory ID of the list

subjects =["eng","maths","sci"]

print(" ".join(subjects))
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)