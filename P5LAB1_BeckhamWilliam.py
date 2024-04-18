# William Beckham
# 04-17-2024
# P5LAB-- vending machine
# Overview:
# This program simulates a vending machine system where users can browse items, add them to a cart, and
# checkout using either cash or credit. Admins can manage the inventory, update prices, add new items,
# view machine's current and total transactions, and withdraw all cash from the machine.


# password 'admin123'


import getpass
import pickle


# Global Variables
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
TAX_RATE = 0.02
total_money_in = 75000  # Starting money in the machine in cents
total_money_out = 0
total_money_in_today = 0  # Total money put into the machine today in cents

# Function to save the grocery list and any changes to it to a database file
def save_database():
    """
    Save the grocery list and any changes to a database file.

    Returns:
        None
    """
    try:
        with open("grocery_database.pkl", "wb") as file:
            pickle.dump(avail_items, file)  # Serialize avail_items and write to file
        print("Database saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving database: {e}")

        
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
    Add items to cart by selecting numbers and display running total.

    Args:
        cart (list): List to store selected items.
        items (dict): Dictionary containing items and their prices.

    Returns:
        None
    """
    total = 0
    while True:
        show_avail_items(items)  # Show available items
        print("Running Total: $%.2f" % (total / 100))  # Display running total
        selection = input("Enter the number of the item to add (or 'cancel' to cancel transaction): ")
        if selection.lower() == "cancel":
            break
        elif selection.isdigit():
            index = int(selection) - 1
            if 0 <= index < len(items):
                item = list(items.keys())[index]
                cart.append(item)
                total += items[item]  # Update running total
                print(f"{item.capitalize()} added to cart.")
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


# Function to display cart with running total
def display_cart(cart, items):
    """
    Display items in the cart along with the running total.

    Args:
        cart (list): List containing selected items.
        items (dict): Dictionary containing items and their prices.

    Returns:
        None
    """
    print("\nYour Cart:")
    total = 0
    for item in cart:
        total += items[item]
        print(f"{item.capitalize()} - ${items[item] / 100:.2f}")
    print(f"\nRunning Total: ${total / 100:.2f}")


# Function to calculate change in dollars, quarters, dimes, nickels, and pennies
def checkout_process(cart):
    """
    Handle the checkout process.

    Args:
        cart (list): List containing selected items.

    Returns:
        None
    """
    global total_money_out, total_money_in_today, total_money_in

    # Calculate total price of items in the cart
    subtotal = calculate_total(cart, avail_items)

    # Calculate tax
    tax = subtotal * TAX_RATE

    # Display receipt
    print("\nReceipt:")
    display_cart(cart, avail_items)
    print(f"\nSubtotal: ${subtotal / 100:.2f}")
    print(f"Tax: ${tax / 100:.2f}")

    while True:
        payment_method = input("Select payment method (cash/credit): ").lower()
        if payment_method == "credit":
            total_price = subtotal + tax
            print(f"Total to pay: ${(total_price / 100):.2f}")
            amount_paid = 0  # No need to input amount for credit card payment

            if total_price > total_money_in:
                print("Error: Insufficient funds in the machine for cashback.")
                return

            while True:
                cashback_choice = input("Do you want cashback? (yes/y or no/n): ").lower()
                if cashback_choice in ['yes', 'y']:
                    while True:
                        try:
                            cashback = float(input("Enter the amount of cashback you want (in dollars): "))
                            if 0 <= cashback <= 100:  # $100 maximum cashback
                                break
                            else:
                                print("Invalid amount. Please enter an amount up to $100.")
                        except ValueError:
                            print("Invalid input. Please enter a valid amount.")

                    if cashback > total_money_in:
                        print("Error: Insufficient funds in the machine for cashback.")
                        continue

                    print(f"Cashback requested: ${cashback:.2f}")

                    # Calculate and display cashback breakdown
                    print("\nCashback Dispensed:")
                    print(f"Dollars: {int(cashback)}")

                    # Deduct cashback from total money in the machine
                    total_money_in -= cashback * 100  # Convert cashback to cents and subtract from total money in machine

                    # Add cashback to total money out for the day
                    total_money_out += cashback * 100

                    break
                elif cashback_choice in ['no', 'n']:
                    cashback = 0
                    break
                else:
                    print("Invalid input. Please enter 'yes'/'y' or 'no'/'n'.")

            # Just display a message for credit payment
            print("Thank you for your purchase!")

        elif payment_method == "cash":
            total_price = subtotal + tax
            print(f"Total to pay: ${(total_price / 100):.2f}")

            while True:
                amount_paid_str = input("Enter the amount you are paying: ")
                if '.' not in amount_paid_str:
                    amount_paid_str += '.00'  # Add .00 if not already present

                try:
                    amount_paid = float(amount_paid_str)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
                    continue  # Retry input

                if amount_paid < total_price / 100:
                    print("Insufficient payment. Please input a higher amount.")
                else:
                    break  # Break the loop if the payment is sufficient

            cashback = 0

            # Calculate change
            change = amount_paid - total_price / 100  # Convert total_price to dollars

            if change < 0:
                print("Error: Insufficient payment. Please input a higher amount.")
                return

            # Display change
            print(f"Change: ${change:.2f}")

            # Calculate and display breakdown of change
            dollars, cents = divmod(change, 1)
            cents = round(cents * 100)
            quarters, cents = divmod(cents, 25)
            dimes, cents = divmod(cents, 10)
            nickels, pennies = divmod(cents, 5)

            print("\nChange Breakdown:")
            print(f"Dollars: {int(dollars)}")
            print(f"Quarters: {quarters}")
            print(f"Dimes: {dimes}")
            print(f"Nickels: {nickels}")
            print(f"Pennies: {pennies}")

            # Update total_money_out with change and cashback
            total_money_out += (change + cashback * 100)

            # Subtract change from total money in the machine
            total_money_in -= change * 100

        else:
            print("Invalid payment method. Please select either cash or credit.")
            return

        # Adjust total money in and out to include/exclude cashback
        total_money_in_today += (total_price - cashback * 100)  # Only include total price, excluding cashback


        # Return to the customer menu after the payment process
        return


# Customer menu
def customer_menu(password):
    """
    Customer menu for selecting items, viewing cart, and checking out.

    Args:
        password (str): Admin password.

    Returns:
        None
    """
    while True:
        cart = []
        while True:
            show_avail_items(avail_items)
            print("Enter the number of the item to add to cart (or 'end' to finish): ")
            selection = input().lower()
            if selection == "end":
                break
            elif selection.isdigit():
                index = int(selection) - 1
                if 0 <= index < len(avail_items):
                    item = list(avail_items.keys())[index]
                    cart.append(item)
                    print(f"{item.capitalize()} added to cart.")
                else:
                    print("Invalid number. Please select a valid number from the list.")
            elif selection == "c":
                if cart:
                    print("\nYour Cart:")
                    display_cart(cart, avail_items)
                else:
                    print("Your cart is empty.")
            elif selection == "p":
                if cart:
                    checkout_process(cart)
                    break
                else:
                    print("Your cart is empty. Please add items before checking out.")
            elif selection == "main":
                if confirm_password(password):
                    return  # Return to main menu
                else:
                    print("Incorrect password. Access denied.")
            else:
                print("Invalid input. Please enter a number, 'c' to view cart, 'p' to checkout, or 'end' to finish.")

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
        print(f"Current money in the machine: ${total_money_in / 100:.2f}")

        add_money = input("Do you want to add more money to the machine? (yes/no): ").lower()
        if add_money == "yes":
            try:
                amount_to_add = float(input("Enter the amount to add to the machine in dollars: "))
                if amount_to_add < 0:
                    print("Invalid amount. Please enter a non-negative number.")
                    continue
                total_money_in += amount_to_add * 100  # Convert dollars to cents and add to total_money_in
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
    print(f"Total money put into the machine today: ${total_money_in_today / 100:.2f}")
    print(f"Total money dispensed from the machine today: ${total_money_out / 100:.2f}")

# Function to withdraw all cash from the machine
def withdraw_all_cash():
    """
    Withdraw all cash from the machine and zero out the total money in the machine.

    Returns:
        None
    """
    global total_money_in, total_money_out
    print(f"Withdrawing all cash from the machine: ${total_money_in / 100:.2f}")
    total_money_out += total_money_in
    total_money_in = 0

# Function to confirm password
def confirm_password(password):
    """
    Confirm the admin password.

    Args:
        password (str): Admin password.

    Returns:
        bool: True if password is correct, False otherwise.
    """
    entered_password = getpass.getpass("Enter the password: ")
    return entered_password == password

# Function to delete items from Grocery List
def delete_item_from_grocery_list():
    """
    Delete an item from the Grocery List.

    Returns:
        None
    """
    while True:
        show_avail_items(avail_items)
        item_name = input("Enter the name of the item to delete (or 'end' to finish): ").lower()
        if item_name == "end":
            break
        elif item_name not in avail_items:
            print("Item not found in the Grocery List.")
        else:
            del avail_items[item_name]
            print(f"{item_name.capitalize()} deleted from Grocery List.")

# Admin menu
def admin_menu(password):
    """
    Admin menu for managing the vending machine.

    Args:
        password (str): Admin password.

    Returns:
        None
    """
    if not confirm_password(password):
        print("Incorrect password. Access denied.")
        return

    while True:
        print("\nAdmin Menu:")
        print("1. Add items to Grocery List")
        print("2. Change prices in Grocery List")
        print("3. Delete item from Grocery List")
        print("4. Display current money in the machine and add more money")
        print("5. Display money in and money out of the machine for the day")
        print("6. Display available items")
        print("7. Update all changes")
        print("8. Withdraw all cash from the machine")
        print("9. Return to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_items_to_grocery_list()
        elif choice == "2":
            change_prices_in_grocery_list()
        elif choice == "3":
            delete_item_from_grocery_list()
        elif choice == "4":
            manage_money_in_machine()
        elif choice == "5":
            display_money_in_and_out()
        elif choice == "6":
            show_avail_items(avail_items)
        elif choice == "7":
            update_changes()
        elif choice == "8":
            withdraw_all_cash()
        elif choice == "9":
            print("Returning to Main Menu...")
            break  # Exit the admin menu loop
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


# Function to save the grocery list, total money in machine, and any changes to a database file
def save_database():
    """
    Save the grocery list, total money in machine, and any changes to a database file.

    Returns:
        None
    """
    try:
        with open("vending_machine_database.pkl", "wb") as file:
            data = {"avail_items": avail_items, "total_money_in": total_money_in}
            pickle.dump(data, file)  # Serialize data and write to file
        print("Database saved successfully.")
    except Exception as e:
        print(f"Error occurred while saving database: {e}")

# Main function to run the vending machine program
def main():
    """
    Main function to run the vending machine program.

    Returns:
        None
    """
    global total_money_in, avail_items
    # Initialize total money in the machine without subtracting cashback
    total_money_in = 75000  # Starting money in the machine in cents

    # Load database file if it exists
    try:
        with open("vending_machine_database.pkl", "rb") as file:
            data = pickle.load(file)  # Deserialize data from file
            avail_items = data["avail_items"]
            total_money_in = data["total_money_in"]
        print("Database loaded successfully.")
    except FileNotFoundError:
        print("Database file not found. Starting with default grocery list.")
    except Exception as e:
        print(f"Error occurred while loading database: {e}")

    # Admin password
    password = "admin123"

    while True:
        print("\nMain Menu:")
        print("1. Customer")
        print("2. Admin")
        print("3. Shutdown")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_menu(password)
        elif choice == "2":
            if confirm_password(password):
                admin_menu(password)
            else:
                print("Incorrect password. Access denied.")
        elif choice == "3":
            shutdown = input("Are you sure you want to shutdown? (yes/no): ").lower()
            if shutdown == "yes":
                # Save database before shutting down
                save_database()
                print("Shutting down...")
                return
            elif shutdown == "no":
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
