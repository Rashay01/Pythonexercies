#["Even","Odd"]
#list comprehension if a list is even or odd

numbers = [8, 5, 7, 4, 6, 2]
even_odd_list = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(even_odd_list)