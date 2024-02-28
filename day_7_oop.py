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


# -----------------------------------------Assignment --------------------------
# class Bank:
#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
#         self.transactions = []
#         self.__create_transaction("deposit", balance)

#     def display_balance(self):
#         return f"Your balance is: R{self.balance:,}"

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.__create_transaction("withdraw", amount)
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Unsuccess. Insufficent funds."

#     def deposit(self, amount):
#         self.balance += amount
#         self.__create_transaction("deposit", amount)
#         return f"Success. {self.display_balance()}"

#     def __create_transaction(self, type, amount):
#         if len(self.transactions) > 0:
#             id = self.transactions[-1].get("id", 0) + 1
#         else:
#             id = 1
#         self.transactions.append(
#             {"id": id, "Date": datetime.now(), "Type": type, "Amount": amount}
#         )

#     def print_transactions(self):
#         statment = f"{'id':>6} {'Date':>5} {'Type':>6} {'Amount':>10}"
#         for i, transaction in enumerate(self.transactions):
#             statment = (
#                 statment
#                 + f"\n {i}. {transaction['id']:^3} {transaction['Date']:%d %b}"
#                 + f" {transaction['Type']:^8} {transaction['Amount']:<7,}"
#             )
#         return statment


# # gemma, Dhara, caleb - objects/ instances of object bank
# gemma = Bank(123, "Gemma Porrill", 15_000)
# dhara = Bank(124, "Dhara Kara", 50_001)
# caleb = Bank(125, "Caleb Potts", 100_000)

# # Task 2

# # gemma.display_balance() --> Your balance is: R15,000
# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())


# # Task 3
# # caleb.withdraw(2000)

# print(caleb.withdraw(2_000))
# print(caleb.display_balance())

# # Task 4
# # dhara.deposit(10_000) --> Success. Your Balance is: R60,001
# print(dhara.deposit(10_000))


# # Assignment - Transactions Tomorrow
# # #  id   Date       Type     Amount
# # 1.  1  29 Feb   withdraw       2000
# # 2.  2  1 Mar    deposit        6000
# # 3.  3  3 Mar    deposit        7000

# print(caleb.print_transactions())


# caleb1 = Bank(125, "Caleb Potts", 100_000)
# print("withdraw R2,000")
# print(caleb1.withdraw(2_000))

# print("deposit R4,000")
# print(caleb1.deposit(4_000))

# print("deposit R10,000")
# print(caleb1.deposit(10_000))

# print("withdraw R6,000")
# print(caleb1.withdraw(6_000))

# print()
# print(caleb1.print_transactions())


# -----------------------------------------------------------------------------------------
# crtl + , --> settings


# Enscapsulation  | putting all together in one container | giving acccess
# Calss Variables
# class Bank2:
#     intrest_rate = 0.2

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         # private variable
#         self.__balance = balance

#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,.2f}"

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficent funds"

#     def deposit(self, amount):
#         self.__balance += amount
#         return f"Success. {self.display_balance()}"

#     def apply_intrest_rate(self):
#         self.__balance *= (1 + Bank.intrest_rate)
#         # print(self.display_balance())


# gemma = Bank2(123, "Gemma Porrill", 15_000)
# dhara = Bank2(124, "Dhara Kara", 50_001)
# caleb = Bank2(125, "Caleb Potts", 100_000)

# # after 1 year

# gemma.apply_intrest_rate()
# dhara.apply_intrest_rate()
# caleb.apply_intrest_rate()

# print(gemma.display_balance())
# print(dhara.display_balance())
# print(caleb.display_balance())

# --------------------------------Private variables------------
# class Bank3:
#     intrest_rate = 0.2

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         # private variable
#         self.__balance = balance

#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,.2f}"

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficent funds"

#     def deposit(self, amount):
#         self.__balance += amount
#         return f"Success. {self.display_balance()}"

#     def apply_intrest_rate(self):
#         self.__balance *= 1 + Bank.intrest_rate
#         # print(self.display_balance())


# gemma = Bank3(123, "Gemma Porrill", 15_000)
# dhara = Bank3(124, "Dhara Kara", 50_001)
# caleb = Bank3(125, "Caleb Potts", 100_000)

# print(gemma.name)  # public
# # print(gemma.__balance)#can not private


# -----------------------------Class variables and methods---------------
# class Bank:
#     intrest_rate = 0.2
#     no_accounts = 0

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         # private variable
#         self.__balance = balance
#         Bank.no_accounts += 1

#     # staticmethod ---> no cls, self | normal function
#     @staticmethod  # normal function
#     def get_tatal_no_total_account():
#         return f"In total we have {Bank.no_accounts} accounts"

#     # common method across instance
#     @classmethod  # cls -> cllass
#     def update_intrest_rate(cls, rate):
#         cls.intrest_rate = rate

#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,.2f}"

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficent funds"

#     def deposit(self, amount):
#         self.__balance += amount
#         return f"Success. {self.display_balance()}"

#     def apply_intrest_rate(self):
#         self.__balance *= 1 + Bank.intrest_rate


# gemma = Bank(123, "Gemma Porrill", 15_000)
# dhara = Bank(124, "Dhara Kara", 50_001)
# caleb = Bank(125, "Caleb Potts", 100_000)
# alex = Bank(125, "Alex Lazarus", 100)

# Bank.update_intrest_rate(0.1)

# # Apply intrest
# alex.apply_intrest_rate()
# print(alex.display_balance())


# # Task
# print(Bank.get_tatal_no_total_account())


# Execise
# class Circle:
#     pi = 3.14159  # Class variable

#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(diameter):
#         return Circle(diameter / 2)

#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius

#     def calculate_area(self):
#         return f"The area is: {Circle.pi * (self.radius**2):.2f}"


# class Circle:
#     pi = 3.14159  # Class variable

#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter / 2)

#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius

#     @staticmethod
#     def area(radius):
#         return Circle.pi * radius**2

#     def calculate_area(self):
#         return f"The circle area is: {Circle.area(self.radius):.2f}"


# circle1 = Circle(2)

# # Task 1
# print(Circle.perimeter(10))

# # Task 2
# print(circle1.calculate_area())
# circle_from_dia = Circle.from_diameter(20)
# print(circle_from_dia.calculate_area())


# # Inheritence Animal (base) --> Dog (child)


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "some sound"


# class Dog(Animal):
#     def __init__(self, name, speed):
#         super().__init__(name)
#         self.speed = speed

#     # polymorphism | overinding methods
#     def speak(self):
#         return "woof !!"

#     # methods are attributes
#     def run(self):
#         return "🐶 wags tail !!"

#     def speed_bonus(self):
#         return f"Running at {self.speed * 2} km/h"


# toby = Animal("toby")
# maxy = Dog("maxy", 20)
# print(toby.speak())
# print(maxy.speak())
# print(maxy.name)
# print(maxy.run())
# # print(toby.run()) # attribute error
# print(maxy.speed_bonus())

# ============================================================================================


# create 2 more classes from the bank
# Savings account - more intrest rate = 0.05
# CheckingAccount - withdraw R1
# class Bank:
#     intrest_rate = 0.2
#     no_accounts = 0

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         # private variable
#         self.__balance = balance
#         Bank.no_accounts += 1

#     # staticmethod ---> no cls, self | normal function
#     @staticmethod  # normal function
#     def get_tatal_no_total_account():
#         return f"In total we have {Bank.no_accounts} accounts"

#     # common method across instance
#     @classmethod  # cls -> cllass
#     def update_intrest_rate(cls, rate):
#         cls.intrest_rate = rate

#     def display_balance(self):
#         return f"Your balance is: R{self.__balance:,.2f}"

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return f"Success. {self.display_balance()}"
#         else:
#             return f"Insufficent funds"

#     def deposit(self, amount):
#         self.__balance += amount
#         return f"Success. {self.display_balance()}"

#     def apply_intrest_rate(self):
#         self.__balance *= 1 + self.intrest_rate


# class SavingsAccount(Bank):
#     intrest_rate = 0.05


# class CheckingAccount(Bank):
#     withdrawl_fee = 1

#     # overriding
#     def withdraw(self, amount):
#         return super().withdraw(amount + CheckingAccount.withdrawl_fee)


# # SavingsAccount -  interest_rate = 0.05

# # Task 1
# gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
# gemma.apply_intrest_rate()
# print(gemma.display_balance())  # 1_050
# gemma.display_balance()

# # Task 2
# # CheckingAccount - withdraw  R1
# alex = CheckingAccount(126, "Alex Lazarus", 100)
# print(alex.withdraw(50))
# alex(50)
#  49

# --------------------------------------------------------------------------------
# Magic methods __repr__, __str__


class Bank:
    intrest_rate = 0.2
    no_accounts = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        # protected variable
        self._balance = balance
        Bank.no_accounts += 1

    # staticmethod ---> no cls, self | normal function
    @staticmethod  # normal function
    def get_tatal_no_total_account():
        return f"In total we have {Bank.no_accounts} accounts"

    # common method across instance
    @classmethod  # cls -> cllass
    def update_intrest_rate(cls, rate):
        cls.intrest_rate = rate

    def display_balance(self):
        return f"Your balance is: R{self._balance:,.2f}"

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficent funds"

    def deposit(self, amount):
        self._balance += amount
        return f"Success. {self.display_balance()}"

    def apply_intrest_rate(self):
        self._balance *= 1 + self.intrest_rate


class SavingsAccount(Bank):
    intrest_rate = 0.05


class CheckingAccount(Bank):
    withdrawl_fee = 1

    # overriding
    def withdraw(self, amount):
        """This is for withdraw with a transaction fee"""
        return super().withdraw(amount + CheckingAccount.withdrawl_fee)

    def __str__(self):
        """Human readable output"""
        return f"This account belongs to {self.name} and has a balance of R{self._balance:,}"

    def __repr__(self):
        """DX: string --> class"""
        return f"CheckingAccount({self.acc_no}, '{self.name}', {self._balance})"

    def __add__(self, other):
        return self._balance + other._balance


gemma = SavingsAccount(123, "Gemma Porrill", 1_000)
gemma.apply_intrest_rate()
print(gemma.display_balance())  # 1_050
gemma.display_balance()


alex = CheckingAccount(126, "Alex Lazarus", 100)
caleb = CheckingAccount(126, "Caleb Potts", 100_000)
print(alex.withdraw(50))

print(alex)
print(caleb)
# alex.__str__
print(alex.__repr__())
print(repr(alex))  # better method

# print(alex + caleb) #Unsported so can not add
print(alex + caleb)


# Enscaplation - giving access
