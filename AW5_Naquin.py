users = []

while True:
    print("\n SELECT AN OPTION:")
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("\nEnter choice 1 - 5: ")

    if choice == "1":
        if len(users) == 0:
            print("\nNo users found.")
        else:
            print("\nUser List:")
            for i in range(len(users)):
                print("\n", i + 1, "-", users[i])

    elif choice == "2":
        name = input("\nEnter new user name: ")
        users.append(name)
        print("\nUser added.")

    elif choice == "3":
        if len(users) == 0:
            print("\nNo users to update.")
        else:
            for i in range(len(users)):
                print(i + 1, "-", users[i])
            num = int(input("\nEnter user number to update: ")) - 1
            if 0 <= num < len(users):
                new_name = input("\nEnter new name: ")
                users[num] = new_name
                print("\nUser updated.")
            else:
                print("\nInvalid user number.")

    elif choice == "4":
        if len(users) == 0:
            print("\nNo users to delete.")
        else:
            for i in range(len(users)):
                print("\n", i + 1, "-", users[i])
            num = int(input("\nEnter user number to delete: ")) - 1
            if 0 <= num < len(users):
                users.pop(num)
                print("\nUser deleted.")
            else:
                print("\nInvalid user number.")

    elif choice == "5":
        print("\nExiting program...")
        break

    else:
        print("\nInvalid choice. Try again.")