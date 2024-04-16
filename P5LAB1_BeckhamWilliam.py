# Define avail_items dictionary with product names and prices (in cents)
avail_items = {
    "apples": 369,
    "berries": 400,
    "chocolate": 289,
    "turkey": 699,
    "cheese": 400,
    "pepsi": 189,
    "eggs": 350,
    "bread": 300
}

# Variables to track total money put into and dispensed from the machine
total_money_in = 10000  # Starting money in the machine
total_money_out = 0

# Function to show available items with numbers and prices
def show_avail_items(items):
    """
    Display available items with numbers and prices.

    Args:
        items (dict): Dictionary containing items and their prices.

    Returns:
        None
    """
    print("\n\n")
    print("Grocery List:")
    print("--------------")
    for i, (item, price) in enumerate(items.items(), start=1):
        print(f"{i}. {item.capitalize()} - ${price / 100:.2f}")
    print("--------------")

# Function to add items to cart by selecting numbers
def add_to_cart(cart, items):
    """
    Add items to cart by selecting numbers.

    Args:
        cart (list): List to store selected items.
        items (dict): Dictionary containing items and their prices.

    Returns:
        None
    """
    while True:
        selection = input("Enter the number of the item to add (or 'end' to finish): ")
        if selection.lower() == "end":
            break
        elif selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(avail_items):
                item = list(avail_items.keys())[index]
                cart.append(item)
                print(f"{item.capitalize()} added to cart")
            else:
                print("Invalid number. Please select a valid number from the list.")
        else:
            print("Invalid input. Please enter a number or 'end'.")

# Function to calculate total price
def calculate_total(cart, items):
    """
    Calculate total price of items in the cart.

    Args:
        cart (list): List containing selected items.
        items (dict): Dictionary containing items and their prices.

    Returns:
        int: Total price in cents.
    """
    total = sum(items[item] for item in cart)
    return total

# Function to display cart
def display_cart(cart, items):
    """
    Display items in the cart.

    Args:
        cart (list): List containing selected items.
        items (dict): Dictionary containing items and their prices.

    Returns:
        None
    """
    print("\nYour Cart:")
    for item in cart:
        print(f"{item.capitalize()} - ${items[item] / 100:.2f}")

# Function to calculate change in dollars, quarters, dimes, nickels, and pennies
def calculate_change(change):
    """
    Calculate change in dollars, quarters, dimes, nickels, and pennies.

    Args:
        change (float): Amount of change in dollars.

    Returns:
        tuple: Number of dollars, quarters, dimes, nickels, and pennies.
    """
    dollars = int(change)
    change -= dollars
    quarters = int(change // 0.25)
    change -= quarters * 0.25
    dimes = int(change // 0.1)
    change -= dimes * 0.1
    nickels = int(change // 0.05)
    change -= nickels * 0.05
    pennies = round(change * 100)
    return dollars, quarters, dimes, nickels, pennies

# Function to handle checkout process
def checkout_process(total_price):
    """
    Handle the checkout process.

    Args:
        total_price (float): Total price of items in the cart.

    Returns:
        None
    """
    global total_money_out
    while True:
        try:
            amount_paid = float(input("Enter the amount you are paying: "))
            if amount_paid < total_price / 100:
                print("Insufficient payment. Please input a higher amount.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    change = amount_paid - total_price / 100
    print(f"Payment successful. Change: ${change:.2f}")
    print("Change breakdown:")
    dollars, quarters, dimes, nickels, pennies = calculate_change(change)
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

    # Update total money out
    total_money_out += amount_paid

# Customer menu
def customer_menu():
    """
    Customer menu for selecting items, viewing cart, and checking out.

    Returns:
        None
    """
    global total_money_in
    while True:
        cart = []
        total_price = 0
        while True:
            show_avail_items(avail_items)
            print("Enter the number of the item to add to cart (or 'end' to finish, 'main' to return to main menu): ")
            selection = input().lower()
            if selection == "end":
                break
            elif selection.isdigit():
                index = int(selection) - 1
                if 0 <= index < len(avail_items):
                    item = list(avail_items.keys())[index]
                    cart.append(item)
                    total_price += avail_items[item]
                    print(f"{item.capitalize()} added to cart. Running Total: ${total_price / 100:.2f}")
                else:
                    print("Invalid number. Please select a valid number from the list.")
            elif selection == "c":
                if cart:
                    print("\nYour Cart:")
                    display_cart(cart, avail_items)
                    print(f"Total Price: ${total_price / 100:.2f}")
                else:
                    print("Your cart is empty.")
            elif selection == "p":
                if cart:
                    print("\nYour Cart:")
                    display_cart(cart, avail_items)
                    print(f"\nTotal Price: ${total_price / 100:.2f}")
                    checkout_process(total_price)
                    break
                else:
                    print("Your cart is empty. Please add items before checking out.")
            elif selection == "main":
                return  # Return to main menu
            else:
                print("Invalid input. Please enter a number, 'c' to view cart, 'p' to checkout, 'main' to return to main menu, or 'end' to finish.")

# Main menu
def main_menu():
    """
    Main menu for selecting customer or admin menu, or shutting down the system.

    Returns:
        None
    """
    while True:
        print("\nMain Menu:")
        print("1. Customer Menu")
        print("2. Admin Menu")
        print("3. Shutdown System")
        choice = input("Enter your choice: ")
        if choice == "1":
            customer_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            shutdown_system()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Function to update changes made in the vending machine
def update_changes():
    """
    Save changes made to the vending machine to a file.

    Returns:
        None
    """
    global total_money_in
    try:
        with open("vending_machine_data.txt", "w") as f:
            # Write avail_items dictionary to file
            f.write("avail_items:\n")
            for item, price in avail_items.items():
                f.write(f"{item}:{price}\n")
            # Write total_money_in to file
            f.write(f"total_money_in:{total_money_in}\n")
        print("Changes saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving changes: {e}")

# Function to add items to Grocery List
def add_items_to_grocery_list():
    """
    Add items to the Grocery List.

    Returns:
        None
    """
    while True:
        item_name = input("Enter the name of the item to add (or 'end' to finish): ").lower()
        if item_name == "end":
            break
        elif item_name in avail_items:
            print("Item already exists in the Grocery List.")
        else:
            try:
                item_price = float(input("Enter the price of the item in dollars: "))
                avail_items[item_name] = item_price * 100
                print(f"{item_name.capitalize()} added to Grocery List.")
            except ValueError:
                print("Invalid price. Please enter a valid number.")

# Function to change prices in Grocery List
def change_prices_in_grocery_list():
    """
    Change prices of items in the Grocery List.

    Returns:
        None
    """
    while True:
        show_avail_items(avail_items)
        item_name = input("Enter the name of the item to change the price (or 'end' to finish): ").lower()
        if item_name == "end":
            break
        elif item_name not in avail_items:
            print("Item not found in the Grocery List.")
        else:
            try:
                new_price = float(input(f"Enter the new price of {item_name.capitalize()} in dollars: "))
                avail_items[item_name] = new_price * 100
                print(f"Price of {item_name.capitalize()} updated.")
            except ValueError:
                print("Invalid price. Please enter a valid number.")

# Function to display current money in the machine and add more money
def manage_money_in_machine():
    """
    Display current money in the machine and add more money if necessary.

    Returns:
        None
    """
    global total_money_in
    while True:
        print(f"Current money in the machine: ${total_money_in:.2f}")

        add_money = input("Do you want to add more money to the machine? (yes/no): ").lower()
        if add_money == "yes":
            try:
                amount_to_add = float(input("Enter the amount to add to the machine in dollars: "))
                if amount_to_add < 0:
                    print("Invalid amount. Please enter a non-negative number.")
                    continue
                total_money_in += amount_to_add
                print("Money successfully added to the machine.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif add_money == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Function to display money in and money out of the machine for the day
def display_money_in_and_out():
    """
    Display money in and money out of the machine for the day.

    Returns:
        None
    """
    print(f"Total money put into the machine today: ${total_money_in / 100:.2f}")
    print(f"Total money dispensed from the machine today: ${total_money_out / 100:.2f}")

# Function to handle admin menu
def admin_menu():
    """
    Admin menu for managing the vending machine.

    Returns:
        None
    """
    while True:
        print("\nAdmin Menu:")
        print("1. Add items to Grocery List")
        print("2. Change prices in Grocery List")
        print("3. Display current money in the machine and add more money")
        print("4. Display money in and money out of the machine for the day")
        print("5. Display available items")
        print("6. Update all changes")
        print("7. Return to Main Menu")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_items_to_grocery_list()
        elif choice == "2":
            change_prices_in_grocery_list()
        elif choice == "3":
            manage_money_in_machine()
        elif choice == "4":
            display_money_in_and_out()
        elif choice == "5":
            show_avail_items(avail_items)
        elif choice == "6":
            update_changes()
        elif choice == "7":
            print("Returning to Main Menu...")
            break  # Exit the admin menu loop
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Function to shut down the system
def shutdown_system():
    """
    Shut down the system with user confirmation.

    Returns:
        None
    """
    while True:
        confirm = input("Are you sure you want to shutdown? (yes/no): ").lower()
        if confirm == "yes":
            print("Shutting down system...")
            break
        elif confirm == "no":
            print("Shutdown aborted.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Start the program
if __name__ == "__main__":
    main_menu()
