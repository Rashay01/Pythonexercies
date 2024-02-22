#=======================================================================================
#Lamda functions
print("Lamda functions:")


def sum(a, b):
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
