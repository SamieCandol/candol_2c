from name import get_restaurant_name, ask_yes_no
from display import display_menu, print_receipt
from grades import get_menu_item_id, get_valid_quantity
from average import calculate_order_details, BIG_ORDER_DISCOUNT_RATE

def take_customer_order():
    customer_order = []
    while True:
        print("-" * 50)
        item_id = get_menu_item_id()
        item_quantity = get_valid_quantity()
        customer_order.append([item_id, item_quantity])

        if not ask_yes_no("Do you want to order another item?"):
            break
    return customer_order

def main():
    restaurant_name = get_restaurant_name()
    print("Welcome to " + restaurant_name + "!\n")
    display_menu()

    if not ask_yes_no("\nWould you like to place an order?"):
        print("\nNo problem! Have a great day!")
        return

    customer_order = take_customer_order()
    order_details = calculate_order_details(customer_order)
    print_receipt(order_details, BIG_ORDER_DISCOUNT_RATE)

if __name__ == "__main__":
    main()