#===================================================================================
#task1
#Dry - dont repeat yourself

#lime
#Yes, we do have it

#strawberry
#No, we ran out of stock

# stock1 = "vanilla"
# stock2 = "lime"
# stock3 = "choclate"

# flavour = input("What flavour do you want?: ")
# if (flavour in (stock1, stock2, stock3)):
#   print("Yes, we do have it")
# else:
#   print("No, we ran out of stock")


#===================================================================================
#Task2
# shop_stock = "vanilla, lime, chocolate"

# flavour = input("What flavour do you want?: ")
# stocks = shop_stock.split(", ")
# if (flavour in stocks):
#   print(f"Yes, we do have {flavour}")

# else:
#   print(f"No, we ran out of stock of {flavour}")

#===================================================================================
#Refactored for ternar operators
shop_stock = "vanilla, lime, chocolate"

flavour = input("What flavour do you want?: ")
stocks = shop_stock.split(", ")
ans = "Yes, we do have it"  if flavour in stocks else "No, we ran out of stock"

print(ans)

#in is membership operator
