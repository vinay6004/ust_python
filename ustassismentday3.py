# Predefined items with their prices
items = [
    ("Bread", 40),
    ("Cookies", 80),
    ("Butter", 120),
    ("Cheese", 180),
    ("Yoghurt", 60),
]

# Cart to store selected items
cart = []

def view_items():
    print("Available items:")
    for item in items:
        print(f"Name: {item[0]} Price: {item[1]}")

def add_to_cart():
    item_name = input("Enter the item name: ").strip()
    quantity = int(input("Enter the quantity: "))
    for item in items:
        if item[0].lower() == item_name.lower():
            cart.append((item[0], quantity, item[1], item[1] * quantity))
            print(f"{item_name} added to the cart")
            return
    print(f"{item_name} is not available")

def update_cart():
    item_name = input("Which item would you like to update? ").strip()
    for index in range(len(cart)):
        entry = cart[index]
        if entry[0].lower() == item_name.lower():
            quantity = int(input("Enter the new quantity: "))
            cart[index] = (entry[0], quantity, entry[2], entry[2] * quantity)
            print(f"{item_name} updated in the cart")
            return
    print(f"{item_name} is not in the cart")

def delete_from_cart():
    item_name = input("Select the item to remove: ").strip()
    for index in range(len(cart)):
        entry = cart[index]
        if entry[0].lower() == item_name.lower():
            del cart[index]
            print(f"{item_name} removed from the cart")
            return
    print(f"{item_name} is not in the cart")

def print_bill():
    if not cart:
        print("There are no items in the cart!")
        return
    print("Cart Details:")
    print("Name\tQuantity\tPrice\tTotal")
    total_amount = 0
    for entry in cart:
        print(f"{entry[0]}\t{entry[1]}\t\t{entry[2]}\t{entry[3]}")
        total_amount += entry[3]
    print(f"Total Amount of Bill: {total_amount}")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("Enter 1 for viewing the items")
        print("Enter 2 for adding items to the cart")
        print("Enter 3 for updating items in the cart")
        print("Enter 4 for deleting items from the cart")
        print("Enter 5 for printing the bill")
        print("Enter 6 to exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            update_cart()
        elif choice == "4":
            delete_from_cart()
        elif choice == "5":
            print_bill()
        elif choice == "6":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
