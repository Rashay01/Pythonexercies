books = [
    {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {
        "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {
        "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {
        "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]

#=====================================================================================
#task 1
# best_rated_books = []
# for book in books:
#   if book["rating"] >= 4.7:
#     best_rated_books.append(book["title"])
# print(best_rated_books)

# #=====================================================================================
# #task 2
# #List comphrension
# best_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
# print(best_rated_books)

# #=====================================================================================
# #task 3 order A-Z

# best_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
# best_rated_books.sort()
# print(best_rated_books)

# #Alternative

# best_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
# print(sorted(best_rated_books))

#=====================================================================================
#Exersise 2
#task 1
#ask user What is the product name?
#What is the quantity?
#What is the price?

# inventory = [

#   {"name": "Apple", "quantity": 30, "price": 0.50},

#   {"name": "Banana", "quantity": 20, "price": 0.20}

# ]

# product_name = input("What is the product name? ")
# product_quantity = int(input("What is the quantity? "))
# product_price = float(input("What is the price? "))

# new_product = {"name" : product_name, "quantity" : product_quantity, "price" : product_price}
# inventory.append(new_product)
# print(inventory)

# #=====================================================================================
# #Task 2 if exits update quantity
# #Ask for Quantity

# inventory = [

#   {"name": "Apple", "quantity": 30, "price": 0.50},

#   {"name": "Banana", "quantity": 20, "price": 0.20}

# ]

# product_name = input("What is the product name? ")
# product_quantity = int(input("What is the quantity? "))
# product_price = float(input("What is the price? "))

# for product in inventory:
#   if(product["name"] == product_name):
#     product["quantity"] += product_quantity
#     product["price"] = product_price
#     break

# print(inventory)

# #=====================================================================================
# #Task 3

# inventory = [

#   {"name": "Apple", "quantity": 30, "price": 0.50},

#   {"name": "Banana", "quantity": 20, "price": 0.20}

# ]

# product_name = input("What is the product name? ")
# product_quantity = int(input("What is the quantity? "))
# product_price = float(input("What is the price? "))

# exists = False

# for product in inventory:
#   if(product["name"] == product_name):
#     product["quantity"] += product_quantity
#     product["price"] = product_price
#     exists = True
#     break

# if(exists is False):
#   new_product = {"name" : product_name, "quantity" : product_quantity,
#                  "price" : product_price}
#   inventory.append(new_product)

# print(inventory)

# #=====================================================================================
# inventory = [

#   {"name": "Apple", "quantity": 30, "price": 0.50},

#   {"name": "Banana", "quantity": 20, "price": 0.20}

# ]

# product_name = input("What is the product name? ")
# product_quantity = int(input("What is the quantity? "))
# product_price = float(input("What is the price? "))

# for product in inventory:
#   if(product["name"] == product_name):
#     product["quantity"] += product_quantity
#     product["price"] = product_price
#     exists = True
#     break
# else:                                           #only when break does not happen
#   new_product = {"name" : product_name, "quantity" : product_quantity,
#                  "price" : product_price}
#   inventory.append(new_product)

# print(inventory)

#=======================================NOTES=========================================
# 5 pillars -> good quality
#1. Readablility
#2. Maintability
#3. Extensibility
#4. Testability
#5. Performainc

#=====================================================================================

# guests = [{
#     "name": "Alice",
#     "age": 25,
#     "code": "VIP123"
# }, {
#     "name": "Bob",
#     "age": 17,
#     "code": "VIP123"
# }, {
#     "name": "Charlie",
#     "age": 30,
#     "code": "VIP123"
# }, {
#     "name": "Dave",
#     "age": 22,
#     "code": "GUEST"
# }, {
#     "name": "Eve",
#     "age": 29,
#     "code": "VIP123"
# }]

# blacklist = ["Dave", "Eve"]

# # Output
# # People who are 21 or above and VIP123
# # Blacklist are not allowed

# # ["Alice", "Charlie"]

# # club_list = []
# # for guest in guests:
# #   if(guest["age"] >= 21 and guest["code"] == "VIP123" and guest["name"] not in blacklist):
# #     club_list.append(guest["name"])

# # print(club_list)

# club_list1 = [
#     guest["name"] for guest in guests
#     if (guest["age"] >= 21 and guest["code"] == "VIP123"
#         and guest["name"] not in blacklist)
# ]
# print(club_list1)
# #=====================================================================================

# #Constant CASE
# PASS_CODE = "VIP123"

# club_list1 = [
#     guest["name"] for guest in guests
#     if (guest["age"] >= 21 and guest["code"] == PASS_CODE 
#         and guest["name"] not in blacklist)
# ]
# print(club_list1)

#List comprehension 
#filter the list  - last 

#========================================================================================

# nums = [90, 50, 80]

# # for num in enumerate(nums):
# #   print(num)


# for index, num in enumerate(nums):
#   print(index, num)

#========================================================================================
#Task 1
# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]

# # for employees increase experience by one year 
# for employee in employees:
#   if 'experience' in employee:
#     employee["experience"] += employee["experience"] + 1
#   else:
#     employee["experience"] = 1

# print(employees)


# print()
# print()
# #========================================================================================
# #Task 2
# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]

 
# for employee in employees:
#   employee["experience"] = employee.get("experience", 0) + 1

# print(employees)

# #========================================================================================
# print()
# print()
#Task 3
#senior 5=>
#middle 3= <5
#junior 1=>

# employees = [
#   {"name": "Alex", "experience": 2},
#   {"name": "Gemma"},
#   {"name": "Rashay", "experience": 4},
#   {"name": "Thato"}
# ]


# for employee in employees:
#   employee["experience"] = employee.get("experience", 0) + 1
#   if(employee["experience"] >= 5):
#     employee["status"] = "Senior"
#   elif(5 > employee["experience"] >= 3):
#     employee["status"] = "Mid-Level"
#   else:
#     employee["stauts"] = "Junior"

# print(employees)

#=======================================================================================
# Copy

movie = {
  "name": "Mr Bones",
  "year": 2001,
}

# movie_copy = movie.copy()

#unpacking operator * -> list || ** - dict
# movie_copy2 = {**movie, "rating" : 10}
# print(movie_copy2)

# movie_copy3 = {**movie, "rating" : 10, "year" : 2002}
# print(movie_copy3)

# movie_copy4 = {"rating" : 10, "year" : 2002, **movie}
# print(movie_copy4)

# movie = {
#   "name": "Mr Bones",
#   "year": 2001,
# }

# detail = {
#   "actor" : "Leon",
#   "director" : "Dizthendo"
# }

# movie_details = {**movie, **detail} #preffered
# print(movie_details)

# #-----------------------------List ---------------------------------------------
# price = [1000, 1200, 400]
# price_copy = [*price]
# print(price_copy)

# price_copy1 = [*price, 50, 60]
# print(price_copy1)

# t1 = [80, 90]
# t2 = [50, 100]

# t3 = [*t1, *t2]
# print(t3)

test ={}

test.update(movie)
print(test)