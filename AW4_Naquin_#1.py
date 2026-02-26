def find_target(a, b, c):
    if a > b and a > c:
        print(f"Letter A is the largest number with the value of:{a}")
    elif b > a and b > c:
        print(f"Letter B is the largest number with the value of:{b}")
    else:
        print(f"Letter C is the largest number with the value of:{c}")

a = int(input("Enter a number for letter A:"))
b = int(input("Enter a number for letter B:"))
c = int(input("Enter a number for letter C:"))

find_target(a, b, c)