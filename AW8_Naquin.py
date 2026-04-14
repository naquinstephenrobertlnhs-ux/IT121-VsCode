FILENAME = "message.txt"

try:
    with open(FILENAME, "x") as f:
        print(f"Success: '{FILENAME}' has been created.")
except FileExistsError:
        print(f"Error: File '{FILENAME}' already exists.")
except Exception as e:
        print(f"An Unexpected error occurred! {e}")
    
while True:
    print("------Messenger from TEMU------")
    print("\n1. Send a message")
    print("2. View all messages")
    print("3. Exit")
        
    choice = input("Select an option: ")
        
    if choice == '1':
        msg = input("Enter a message: ")
        try:
            with open(FILENAME, "a") as f:
                f.write(msg + "\n")
            print("Message sent!")
        except Exception as e:
            print(f"Error writing to file: {e}")
        
    elif choice == '2':
        try:
            with open(FILENAME, "r") as f:
                print("---Messages:---")
                print(f.read().strip())
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
                
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
        
