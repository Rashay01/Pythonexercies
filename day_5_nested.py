classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}

#Task 1
#each classes average
a_total =0
b_total =0
for key, value in classes.items():
  for student in value:
    if key == "Class A":
      a_total += sum(student["grades"])/len(student["grades"])
    else:
      b_total += sum(student["grades"])/len(student["grades"])

print(f"Class A average: {a_total/len(classes['Class A']):.2f}")
print(f"Class B average: {b_total/len(classes['Class B']):.2f}")
    
    

#Task2
#each students average
for key, value in classes.items():
  for student in value:
    print(f"{student['name']} average: {sum(student['grades'])/len(student['grades']):.2f}")