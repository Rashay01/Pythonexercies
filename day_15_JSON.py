import json

data = {
    "employees": [
        {"name": "Alice", "age": 30, "department": "Sales"},
        {"name": "Bob", "age": 25, "department": "Marketing"},
    ]
}

print(type(data))
print(data["employees"][0]["age"])


data_json = json.dumps(data, indent=4)
print(data_json, type(data_json))  # Strig
# print(data_json["employees"]) # Type error

# JSON - JavaScript Object Notaion
# 1. Universal Languague
# 2. loose Coupling - if you change yor backed the forntend will not care - front end and backend it is independent
# 3. Platform independent - dont need to chnage server based on platform

# First-Class Function --> Function being treated as a value
sport = {"name": "Dhoni", "dbl": lambda x: x * 2}  # valid Dictionary

print(sport["dbl"](100))

# sport_json = json.dumps(sport) # JSON is not serializable | can not convert Dictionary as it contains a function
# print(sport_json)

student_json1 = """
{
    "name": "gemma",
    "gender": "female"
}"""

stud = json.loads(student_json1)
print(stud["name"])


bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""

# Task 1

# for all active users want to increase the balance by 10%

bank_data_obj = json.loads(bank_data)

for user in bank_data_obj:
    if user["isActive"]:
        user["balance"] = round(user["balance"] * 1.1, 2)

output = json.dumps(bank_data_obj, indent=4)

print(output)

# List comprehension
bank_data_obj1 = json.loads(bank_data)

output1 = json.dumps(
    [
        (
            {**user, "balance": round(user["balance"] * 1.1, 2)}
            if user["isActive"]
            else {**user}
        )
        for user in bank_data_obj1
    ],
    indent=4,
)

print(output1)

# loose coupling - as long as you send json its fine
# tight coupling - you need to rewrie every thing - use to send HTML files everytime

# micro serveice architecture - mixture of multiple backends
# monolith architechture - single architecture
# https://www.youtube.com/watch?v=CZ3wIuvmHeM&ab_channel=InfoQ


# write a file
with open("bank_accounts.json", "w") as file:
    json.dump(output1, file, indent=4)

# read a file
with open("bank_accounts.json", "r") as file:
    data = json.load(file)
    print(data, type(data))


# create post summary.json  return amount of comments

# {
#   "posts_summary": [
#     {
#       "title": "The Future of AI",
#       "author": "Alice",
#       "number_of_comments": 3
#     },
#     {
#       "title": "Learning Python",
#       "author": "Bob",
#       "number_of_comments": 1
#     },
#     {
#       "title": "Web Development Trends",
#       "author": "Charlie",
#       "number_of_comments": 0
#     }
#   ]
# }

ans = None

with open("blog_post.json", "r") as file:
    ans = json.load(file)

output3 = [
    {
        "title": post["title"],
        "author": post["author"],
        "number_of_comments": len(post["comments"]),
    }
    for post in ans["posts"]
]

with open("post_summary.json", "w") as file:
    json.dump(output3, file, indent=4)
