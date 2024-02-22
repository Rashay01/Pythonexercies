#=======================================================================================
#Lamda functions
print("Lamda functions:")


def sum1(a, b):
  return a + b


# one line functions
add = lambda a, b: a + b  #rule 1 - see below

print(add(6, 7))

# Anonymous - nameless function
# one liner
# implicitly return (automatically)

#functions are treated first class citizen:
# 1. Assign a function to a variable
# 2. Pass a function as a argument
# 3. Returns a function

player_stats = [10, 30, 60]

boosted_stats = map(lambda x: x * 2, player_stats)
print(list(boosted_stats))

double_values = lambda x: x * 2
boosted_stats1 = map(double_values, player_stats)
print(list(boosted_stats1))


def square(x):
  return x * x


super_boosted_stats = map(square, player_stats)
print(list(super_boosted_stats))

super_boosted_stats = map(lambda x: (x[0] + x[1]) * 2, [(10, 6), (60, 4),
                                                        (12, 2)])
print(list(super_boosted_stats))

super_boosted_stats = map(lambda x: x * 2, [(10, 6), (60, 4), (12, 2)])
print(list(super_boosted_stats))


#higher oder function
def greeting(hello_message, name):
  print(hello_message() + name)


def say_hello():
  return "Hello, "


greeting(say_hello, "Caleb")


#HOF
def map_own(fn, arr):
  return [fn(a) for a in arr]


arr = [1, 2, 3, 4, 5]
print(map_own(lambda x: x * 2, arr))
print(arr)

#map object -> lazy | efficent


#3
def sayHello1():
  def msg():
    return "hello, 🎊"
  return msg

print(sayHello1()())

#implicit return - lambda x returns lambda y | factory of functions
#curring, Partials - Assignment
#Functional programming - F#, Herskel (no loops)
# Curring, HOF, Recursion
#OOP programing - inheritence
#Procedural programming
#Mathematical programming 

mul = lambda x: lambda y: x*y 

print(mul(3)(6))



#HOF - argument is a function
result1 = map(lambda x: x * 2,[10, 30, 60])
result2 = filter(lambda x:x >10, [10, 50, 60, 100, 6, 8 ,30])
print(list(result2))

# Pythonic way 
print(sum([10,30,60]))

#Sequence - List,
#1. len()
#2. sum()
#3. sorted()
#4. max()
#5. min()

print(max([10,30,60]))
print(min([10,30,60]))

print(all([True, False, True])) #all
print(any([True, False, True])) # or

print(all([10,0,-1])) 
# falsy values| converted to Boolean it is False -> 0, None, [], {}, set(), "", ()
# Other values are Truthly

x=[] 
#if requires a boolean 

if(x):
  print("cool")
else:
  print("super")