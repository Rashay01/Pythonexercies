
#Vs code shortcut crt + shift + p -> command
#ctrl + p -> find file

# Lexical scope 
# def market():
#     price = 100
#     def get_price():
#         print("The price is: ", price)
#     get_price()

# market()

#Scope: Lifetime of a variable 
# def cool():
#     x = 10              # x lifeline is till the end of function
#     print('super')

# cool()
# print("The value of x", x) # x is undefined and outside of scope


code_word = "Hulk"

def space_ship():
    question ="please provide code word"

    def code_word_check():
        password = "Hulk"
        print(question)

        if(password == code_word):
            print(f"Welcome, {password} the strongest avenger")
        else:
            print("Access denied")
    code_word_check()

space_ship()



def add(x):
    def add1(y):
        return x + y
    return add1

print(add(10)(5))


# Default value copy by refrence

def fun(nums=[]):
    nums.append(10)
    print(nums)

fun()
fun()
fun()
fun()

def fun(nums = None):
    if (nums == None):
        nums =[]
    nums.append(10)
    print(nums)

fun()
fun()
fun()
fun()
