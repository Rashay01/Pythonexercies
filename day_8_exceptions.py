from datetime import datetime


def math_divide(n1, n2):
    try:
        result = n1 / n2
        print("The answer is ", result)
    except ZeroDivisionError:
        print("You cannot divide by zero! 💀")
    else:
        # when no errors happens
        print("Division was successful")
    finally:
        # Always executes
        print("Operation done")


# def calculate_age():
#     birth_year = int(input("Please tell me your year of birth? 2"))
#     curr_year = datetime.today().year
#     return f"Your age is {curr_year-birth_year} "

# def calculate_age():
#     try:
#         birth_year = int(input("Please tell me your year of birth? 2"))
#         if birth_year >= 0:
#             return "Please enter a positive number"

#         curr_year = datetime.today().year
#         if birth_year > curr_year:
#             return f"Please enter a year that is {curr_year} or lower"

#         return f"Your age is {curr_year-birth_year} "
#     except ValueError:
#         print("Please enter a year in format (YYYY)")


def calculate_age():
    try:
        user_input = input("Please tell me your year of birth? ")
        birth_year = int(user_input)
        curr_year = datetime.today().year
        if birth_year <= 0:
            # Handelling logical error
            # raise --> Stops further execution
            raise ValueError("Year cannot be negative")
        if birth_year > curr_year:
            raise ValueError("Year cannot be more than current year")
        print(f"Your age is {curr_year-birth_year} ")
    except ValueError as e:
        print("Invalid number: ", e)
    except Exception as err:
        print("Error: ", err)


# Creating your own Error class
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed "
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.value} --> {self.message}"


def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)
    # match what type of error
    except NegativeNumberError as e:
        print(e)


if __name__ == "__main__":
    # math_divide(10, 5)
    # math_divide(20, 5)
    # math_divide("abc", 5)
    # print("Hiii")
    # calculate_age()
    only_positive_num()
