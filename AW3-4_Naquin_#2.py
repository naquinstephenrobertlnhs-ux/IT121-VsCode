x = 300
def closet_number(x):
    
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))

    number1 = abs(x - a)
    number2 = abs(x - b)
    number3 = abs(x - c)

    if number1 == number2 == number3:
        print(f"A is {a}, B is {b}, and C with the number value of {c} are all equal. Therefore all numnber are the closest to {x}")
    elif number1 <= number2 and number1 <= number3:
        print(f"Letter A with the number value of {a} is the closest to {x}")
    elif number2 <= number1 and number2 <= number3:
        print(f"Letter B with the number value of {b} is the closest to {x}")
    else:
        print(f"Letter C with the number value of {c} is the closest to {x}")

closet_number(x)
