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


math_divide(10, 5)
math_divide(20, 5)


print("Hii")
