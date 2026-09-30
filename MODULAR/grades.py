from display import MENU

def get_menu_item_id():
    while True:
        id_input = input("Enter the item ID: ").strip()
        if id_input.isdigit() and int(id_input) in MENU:
            return int(id_input)
        print("  >> Invalid item ID. Please enter a valid ID from the menu.")

def get_valid_quantity():
    while True:
        quantity_input = input("Enter the quantity: ").strip()
        if quantity_input.isdigit() and int(quantity_input) > 0:
            return int(quantity_input)
        print("  >> Invalid quantity. Please enter a whole number greater than 0.")