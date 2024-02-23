a = 8
b = 10

print("The sum is:", a + b)

a1 = 10
b1 = 20

print("The sum is:", a1 + b1)


#=====================================Functions======================================

#function are way to pack your logic
# No return = None

#declaration/ Defination  - whole thing under 
#(a,b) is your parameters/ arguments 
def sum(a, b):
  return a + b   #function body - more than one 
#Abstraction the logic | Hiding implemntation 


#Abstraction ( hiding implematation) - logic 
print("The sum is: ",sum(30,50))


# Default values - arument/s should be at the end

def driving_test(name, age, car = "Toyota tazz"):
  if age >= 18:
    return f"{name} eligible for driving. You will be tested with {car}"
  else:
    return "Try again after few years 👶🍼"
  

print(driving_test("Caleb",20, "GR Corolla"))
#print(driving_test(10))
print(driving_test("Gemma",20))


# Types of arguments:
# Position argument - based on whre the position is 
# Keyword argument

#print(driving_test(21,"Dhara")) #TypeError will occur

#Keyword argument
print(driving_test(age=21,name="Dhara")) 

def driving_test1(name, age=15, car = "Toyota tazz"):
  if age >= 18:
    return f"{name} eligible for driving. You will be tested with {car}"
  else:
    return "Try again after few years 👶🍼"

print(driving_test1("Gemma")) #order matters - position arguments

#Pass allows you still call the function without the function body
def func_name( test1, test2):
  pass

func_name(1,2)


