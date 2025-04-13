# define the main function to call the add_inventory and remove_widget_inventory functions

import dictionary

def main():
    inventory = {}

    while True:
        print("Inventory Menu:")
        print("1 - Add/Update Widget")
        print("2 - Remove Widget")
        print("3 - Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            widget_name = input("Enter the widget name to add/update: ")
            quantity_input = input("Enter the quantity to add: ")

            dictionary.add_inventory(inventory, widget_name, quantity_input)
            print(f"{widget_name} updated. New quantity: {inventory[widget_name]}")
            dictionary.print_inventory(inventory)

        elif choice == '2':
            widget_name = input("Enter the widget name to remove: ")
            result = dictionary.remove_inventory_widget(inventory, widget_name)
            print(result)
            dictionary.print_inventory(inventory)

        elif choice == '3':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()