def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter the item name: ")
            shopping_list.append(item_name)
            print(f"{item_name} added to the list.")
        elif choice == '2':
            item_name = input("Enter the item name to remove: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print(f"{item_name} removed from the list.")
            else:
                print(f"{item_name} not found in the list.")
        elif choice == '3':
            if not shopping_list:
                print("The list is empty.")
            else:
                # print("Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
