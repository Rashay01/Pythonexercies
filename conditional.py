# lexical order

#get two people heights 
person1 = input("Please provide your name: ")
height1 = float(input("Please provide your height in cm: "))
person2 = input("Please provide your name: ")
height2 = float(input("Please provide your height in cm: "))

if (height1 > height2):
  print(f"{person1} is taller")
elif (height1 == height2):
  print(f"{person1} and {person2} are of same height")
else:
  print(f"{person2} is taller")

#elif - many | else - one
