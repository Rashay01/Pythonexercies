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
