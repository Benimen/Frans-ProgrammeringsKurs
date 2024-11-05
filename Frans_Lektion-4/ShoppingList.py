available_items = ["Milk", "Bread", "Egg", "Butter", "Cheese", "Apple", "Banana", "Cola", "Powerking"]

def Show_Menu():
    print("Shopping list")
    print("1. Add item to shopping cart.")
    print("2. Show all cart items")
    print("3. Show all items")
    print("4. Remove item from cart")
    print("5. Save list to file")
    print("6. Exit program")

def show_available_items():
    print("Available items:")
    for idx, item in enumerate(available_items, 1):
        print(f"{idx}. {item}")


def add_item(cart):
    show_available_items()
    try:
        choice = int(input("Number of items to add to cart: ")) - 1
        if 0 <= choice < len(available_items):
            item = available_items[choice]
            try:
                quantity = int(input(f"Enter quantity of {item} to add: "))
                if quantity < 1:
                    print("Please enter a positive number.")
                else:
                    if item in cart:
                        cart[item] += quantity
                    else:
                        cart[item] = quantity
                    print(f"{quantity} of {item} have been added to the cart.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Please enter a valid quantity.")
    except ValueError:
        print("Please enter a valid number.")


def show_cart_items(cart):
    if cart:
        print("Items in your cart:")
        for item, quantity in cart.items():
            print(f"{item} x {quantity}")
    else:
        print("Shopping list is empty")


def delete_item(cart):
    show_cart_items(cart)
    item_to_remove = input("Name of item to remove: ")
    if item_to_remove in cart:
        try:
            quantity_to_remove = int(input(f"Quantity to remove (1 - {cart[item_to_remove]}): "))
            if quantity_to_remove < 1:
                print("Please enter a positive number.")
            elif quantity_to_remove >= cart[item_to_remove]:

                del cart[item_to_remove]
                print(f"All of {item_to_remove} have been removed from the cart.")
            else:

                cart[item_to_remove] -= quantity_to_remove
                print(f"{quantity_to_remove} of {item_to_remove} have been removed from the cart.")
        except ValueError:
            print("Give a valid number.")
    else:
        print("Item not found in cart.")

def save_cart_to_file(cart):
    filename = input("Give a filename to save the cart to file (include '.txt'): ")
    try:
        with open(filename, "w") as file:
            for item, quantity in cart.items():
                file.write(f"{item} x{quantity}\n")
        print(f"Shopping cart have been saved to {filename}.")
    except Exception as e:
        print(f"A error occurred when trying to save {e}")


def Main():
    cart = {}

    while True:
        Show_Menu()
        option = input("Choose an option (1-6): ")

        if option == "1":
            add_item(cart)
        elif option == "2":
            show_cart_items(cart)
        elif option == "3":
            show_available_items()
        elif option == "4":
            delete_item(cart)
        elif option == "5":
            save_cart_to_file(cart)
        elif option == "6":
            print("You exited the program.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    Main()