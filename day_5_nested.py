from pprint import pprint

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

#Variables:
#1.Keywords -> for, class,
#2. 1city = "Cape Town" 
#3. Case sensituve
#4. no special charcters *&(%)- | allowed _
#Task 1
#each classes average

    
    

# #Task2
# #each students average



# class_b ={}
# class_a ={}
# for key, value in classes.items():
#   for student in value:
#     if key == "Class A":
#       class_a = {**class_a, student['name']: float(f"{sum(student['grades'])/len(student['grades']):.2f}")}
#     else:
#       class_b = {**class_a, student['name']: f"{sum(student['grades'])/len(student['grades']):.2f}"}


# output = {"Class A" : class_a, "Class B" : class_b}
# pprint(output)

#Task 1

output = {}
for key, value in classes.items():
  total = 0
  for student in value:
    total+= sum(student["grades"])/len(student["grades"])
  ans = float(f"{total/len(value):.2f}")
  output = {**output, key: ans}

pprint(output)


#---------------------------------Model ans-----------------------------------
def find_avg(nums):
  return float(f"{sum(nums)/len(nums):.2f}")

output_ans = {}
for cls_name, students in classes.items():
  class_avg =[]
  for student in students:
    class_avg.append(find_avg(student.get("grades",[])))
  output_ans[cls_name] = find_avg(class_avg)

pprint(output_ans)

#Task 2
output1 = {}
for key, value in classes.items():
  avg_class_student ={}
  for student in value:
    avg_class_student[student['name']] = find_avg(student['grades'])
  output1[key] = avg_class_student

pprint(output1)

#Task 3 -> nested comrehension
#using list comprehension get the average of grade of each class
output3 =  {key: find_avg([find_avg(student["grades"]) for student in students]) for key, students in classes.items()}
pprint(output3)

#Task 4.2
students_avg_dict = {cls_name: {student['name'] : find_avg(student['grades']) for student in students} for cls_name, students in classes.items()}
pprint(students_avg_dict)

#Task 4.1
students_avg_dict = {}
for cls_name, students in classes.items():
  students_avg_dict[cls_name]= {student['name'] : find_avg(student['grades']) for student in students}

