#===================================================================================
# Task -> Farhenhiet to Celcius

#declration
# farenheit = input("Please provide your Farenheit: ")

# celcius = (float(farenheit) - 32) * 5/9

# print("The " + str(farenheit) + "°F is: " + str(celcius) + "°C")
# print(f"The {farenheit}°F is:{celcius} °C")

#{} - interpolation

#===================================================================================
#Task -> Find the age of the perso if the birth year is given

# import datetime

# birth_year = input("What year are you born in? ")
# curr_year = datetime.date.today().year
# curr_age = curr_year - int(birth_year)
# print(f"Your age is: {curr_age}")

#===================================================================================
#Task given the radius give the area of the circle

# import math

# radius = input("radius of circle")
# area_circle = math.pi * float(radius) ** 2
# print(f"The area of the circle is {area_circle}")

#Task -> Build a loader
# percentage = input("Please provide your percentage: ")
# progress = float(percentage)//10
# bar = "=" * int(progress)
# empty = " " * (10 - int(progress))
# print(f"[{bar}{empty}] {percentage}%")

x = None #NUll initilisation 