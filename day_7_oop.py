from datetime import datetime

# Object Orientated Programming?


# Car
# 1. engine
# 2. wheels
# 3. doors
# 4. name

# Car -> ferrari
# 1. engine - v8
# 2. wheels - 4
# 3. doors  - 2

# Car -> Toyata Tazz
# 1. engine - v4
# 2. wheels - 4
# 3. doors  - 4

# Bad way
# class Car:
#     pass

# ferrari = Car()
# ferrari.name = "Ferrari"
# ferrari.engine = "v4"
# ferrari.wheels = 4
# ferrari.doors = 2

# toyata = Car()
# toyata.name = "Ferrari"
# toyata.engine = "v4"
# toyata.wheels = 4
# toyata.doors = 2


# Car --> Blueprint | Class blueprint object
# DRY
class Car:
    def __init__(self, name, engine, wheels, doors):
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors

    def horn(self):
        return "Vroom Vroom"


# self --> to the object created
# ferrari --> object

ferrari = Car("Ferrari", "v4", 4, 2)
toyota = Car("Toyota", "v4", 4, 4)
audi = Car("Audi", "v4", 4, 2)
MercedesBenz = Car("Mercedes-Benz", "v4", 4, 4)

print(ferrari.name, ferrari.wheels)
print(toyota.name, toyota.wheels)
print(ferrari.horn())
print(toyota.horn())

# Bank Account
# 1. account no
# 2. name
# 3. balance

# class  Bank:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     def display_balance(self):
#         return f"Your balance is: R{self.balance:,}"

#     def withdraw(self, amount):
#         if (self.balance> amount):
#             self.balance -= amount
#             return f"Success. Your Balance is: R{self.balance:,}"
#         else:
#             return f"Unsuccess. Your Balance is: R{self.balance:,}"

#     def deposit(self, amount):
#         self.balance += amount
#         return f"Success. Your Balance is: R{self.balance:,}"

# -----------------------------------------------------------------------------
# PEP 8 - Python Enchancements proposals


class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []
        self.create_transaction("deposit", balance)

    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.create_transaction("withdraw", amount)
            return f"Success. Your Balance is: R{self.balance:,}"
        else:
            return f"Unsuccess. Your Balance is: R{self.balance:,}"

    def deposit(self, amount):
        self.balance += amount
        self.create_transaction("deposit", amount)
        return f"Success. Your Balance is: R{self.balance:,}"

    def create_transaction(self, type, amount):
        if len(self.transactions) > 0:
            id = self.transactions[-1].get("id", 0) + 1
        else:
            id = 1
        self.transactions.append(
            {"id": id, "Date": datetime.now(), "Type": type, "Amount": amount}
        )

    def print_transactions(self):
        statment = f"{'id':>6} {'Date':>5} {'Type':>6} {'Amount':>10}"
        for i, transaction in enumerate(self.transactions):
            statment = (
                statment
                + f"\n {i}. {transaction['id']:^3} {transaction['Date']:%d %b}"
                + f" {transaction['Type']:^8} {transaction['Amount']:<7,}"
            )
        return statment


gemma = Bank(123, "Gemma Porrill", 15_000)
dhara = Bank(124, "Dhara Kara", 50_001)
caleb = Bank(125, "Caleb Potts", 100_000)

# Task 2

# gemma.display_balance() --> Your balance is: R15,000
print(gemma.display_balance())
print(dhara.display_balance())
print(caleb.display_balance())


# Task 3
# caleb.withdraw(2000)

print(caleb.withdraw(2_000))
print(caleb.display_balance())

# Task 4
# dhara.deposit(10_000) --> Success. Your Balance is: R60,001
print(dhara.deposit(10_000))


# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000

print(caleb.print_transactions())


caleb1 = Bank(125, "Caleb Potts", 100_000)
print("withdraw R2,000")
print(caleb1.withdraw(2_000))

print("deposit R4,000")
print(caleb1.deposit(4_000))

print("deposit R10,000")
print(caleb1.deposit(10_000))

print("withdraw R6,000")
print(caleb1.withdraw(6_000))

print()
print(caleb1.print_transactions())
