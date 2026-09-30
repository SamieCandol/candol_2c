from datetime import datetime
from name import RESTAURANT_NAME

MENU = {
    1: {"name": "Haraya Lumpia", "price": 150.00},
    2: {"name": "Crispy Kare-Kare Bites", "price": 200.00},
    3: {"name": "Ube Glazed Chicken", "price": 140.00},
    4: {"name": "Lechon Belly sa Apoy", "price": 300.00},
    5: {"name": "Seafood Aligue Pasta", "price": 365.00},
    6: {"name": "Ube Tres Leches", "price": 85.00},
    7: {"name": "Mango-Halong Halo", "price": 95.00},
    8: {"name": "Haraya Sunset drinks", "price": 157.00},
    9: {"name": "Amihan Cooler drinks", "price": 120.00},
    10: {"name": " Coconut and creamy ube", "price": 70.00},
}

def display_menu():
    print("=" * 50)
    print(f"{RESTAURANT_NAME:^50}")
    print("=" * 50)
    print(f"{'ID':<5}{'MENU ITEM':<28}{'PRICE':>17}")
    print("-" * 50)

    for item_id in MENU:
        item_name = MENU[item_id]["name"]
        item_price = MENU[item_id]["price"]
        print(f"{item_id:<5}{item_name:<28}{'P' + format(item_price, '.2f'):>17}")

    print("=" * 50)

def print_receipt(order_details, big_order_discount_rate):
    itemized_list = order_details["itemized_list"]
    current_datetime = datetime.now().strftime("%B %d, %Y  %I:%M %p")

    print("\n")
    print("*" * 50)
    print(f"{RESTAURANT_NAME:^50}")
    print(f"{'123 Sample Street, Cebu City':^50}")
    print("*" * 50)
    print(f"Date: {current_datetime}")
    print("-" * 50)
    print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>10}{'TOTAL':>15}")
    print("-" * 50)

    for entry in itemized_list:
        item_name, item_quantity, item_price, item_total, discount_note = entry
        print(f"{item_name:<20}{item_quantity:>5}{item_price:>10.2f}{item_total:>15.2f}")
        if discount_note:
            print(f"{discount_note:>50}")

    print("-" * 50)
    print(f"{'Subtotal:':<35}{order_details['subtotal']:>15.2f}")

    if order_details["big_order_discount"] > 0:
        discount_label = f"Loyalty Discount (-{int(big_order_discount_rate * 100)}%):"
        print(f"{discount_label:<35}{-order_details['big_order_discount']:>15.2f}")

    print("=" * 50)
    print(f"{'TOTAL:':<35}{order_details['final_total']:>15.2f}")
    print("=" * 50)
    print(f"{'Thank you for ordering with us!':^50}")
    print(f"{'Please come again!':^50}")
    print("*" * 50)