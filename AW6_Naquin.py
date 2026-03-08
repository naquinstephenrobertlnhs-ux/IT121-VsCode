class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self):
        item = input("\nEnter item to add: ")
        self.cart.append(item)
        print("\n", item, "added to cart.")

    def remove_item(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        self.view_cart()
        item = input("\nEnter item to remove: ")
        if item in self.cart:
            self.cart.remove(item)
            print("\n", item, "removed from cart.")
        else:
            print("Item not found.")

    def view_cart(self):
        if not self.cart:
            print("\nCart is empty.")
        else:
            print("\nItems in cart:")
            for item in self.cart:
                print("\n-", item)

    def checkout(self):
        if not self.cart:
            print("\nCart is empty.")
        else:
            print("\nChecking out the following items:")
            for item in self.cart:
                print("-", item)
            print("\nThank you for shopping!")
            self.cart.clear()


cart = ShoppingCart()

while True:
    print("\nShopping Cart Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        cart.add_item()
    elif choice == "2":
        cart.remove_item()
    elif choice == "3":
        cart.view_cart()
    elif choice == "4":
        cart.checkout()
    elif choice == "5":
        print("\nProgram ended.")
        break
    else:
        print("\nInvalid choice.")