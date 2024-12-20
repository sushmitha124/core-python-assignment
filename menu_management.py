class menu_management:
    def add_menu_item(menu, item):
        if item not in menu:
            menu.append(item)
        else:
            print(f"{item} is already in the menu.")
    def remove_menu_item(menu, item):
        if item in menu:
            menu.remove(item)
        else:
            print(f"{item} does not exist in the menu.")

    def check_menu_item(menu, item):
        if item in menu:
            return f"{item} is available"
        else:
            return f"{item} is not available"
obj=menu_management
initial_menu = eval(input("Enter the items in menu"))
add_item = input("Enter item to be added to the menu")
remove_item = input("Enter item to be removed from the menu")
check_item = input("Enter item to check whether it is available in menu")

# Update menu
print("Initial menu:", initial_menu)
obj.add_menu_item(initial_menu, add_item)
obj.remove_menu_item(initial_menu, remove_item)
availability = obj.check_menu_item(initial_menu, check_item)
print("Updated menu:", initial_menu)
print("Availability:", availability)
