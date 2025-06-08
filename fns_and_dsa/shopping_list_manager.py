def display_menu():
    """
    Displays the menu options to the user.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Manages adding, removing, and displaying items in the shopping list.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True: # Loop indefinitely until the user chooses to exit
        display_menu() # Show the menu to the user
        choice = input("Enter your choice: ") # Get user's menu choice

        if choice == '1':
            # Option to add an item
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add) # Add the item to the list
            print(f"'{item_to_add}' has been added to your list.")
        elif choice == '2':
            # Option to remove an item
            if not shopping_list:
                print("Your list is empty. Nothing to remove.")
                continue # Skip to the next loop iteration
            
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove) # Remove the first occurrence of the item
                print(f"'{item_to_remove}' has been removed from your list.")
            else:
                print(f"'{item_to_remove}' not found in your list.")
        elif choice == '3':
            # Option to view the list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                # print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to add numbers to items
                    print(f"{i}. {item}")
                # print("--------------------------")
        elif choice == '4':
            # Option to exit the program
            print("Goodbye!")
            break # Exit the while loop
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



























































