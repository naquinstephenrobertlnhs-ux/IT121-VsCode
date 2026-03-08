while True:
    password = str(input("Enter the password: "))
    
    has_letter = False
    has_number = False

    for ch in password:
        if ch.isalpha():
            has_letter = True
        elif ch.isdigit():
            has_number = True

    if has_letter and has_number:
        print("Password Accepted!")
        break
    else:
        print("Password must contain at least one letter and one number. Please try again.")