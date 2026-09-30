from datetime import datetime

class RestaurantOrderSystem:
    def __init__(self):
        # 1. Initialize restaurant data and configuration inside the constructor
        self.restaurant_name = "HARAYA RESTAURANT "
        self.menu = {
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
        self.bulk_threshold = 5
        self.bulk_discount_rate = 0.05
        self.big_order_threshold = 500.00
        self.big_order_discount_rate = 0.10

    def display_menu(self):
        # 2. Print the menu neatly
        print("=" * 50)
        print(f"{self.restaurant_name:^50}")
        print("=" * 50)
        print(f"{'ID':<5}{'MENU ITEM':<28}{'PRICE':>17}")
        print("-" * 50)

        for item_id, details in self.menu.items():
            print(f"{item_id:<5}{details['name']:<28}{'P' + format(details['price'], '.2f'):>17}")

        print("=" * 50)

    def ask_yes_no(self, question):
        # 3. Handle yes/no loops safely
        while True:
            answer = input(f"{question} (y/n): ").strip().lower()
            if answer in ("y", "yes"):
                return True
            elif answer in ("n", "no"):
                return False
            else:
                print("  >> Invalid input. Please type 'y' or 'n'.")

    def get_menu_item_id(self):
        # 4. Validate item ID input
        while True:
            id_input = input("Enter the item ID: ").strip()
            if id_input.isdigit() and int(id_input) in self.menu:
                return int(id_input)
            print("  >> Invalid item ID. Please enter a valid ID from the menu.")

    def get_valid_quantity(self):
        # 5. Validate quantity input
        while True:
            quantity_input = input("Enter the quantity: ").strip()
            if quantity_input.isdigit() and int(quantity_input) > 0:
                return int(quantity_input)
            print("  >> Invalid quantity. Please enter a whole number greater than 0.")

    def take_customer_order(self):
        # 6. Loop to collect multiple items into an order list
        customer_order = []
        while True:
            print("-" * 50)
            item_id = self.get_menu_item_id()
            item_quantity = self.get_valid_quantity()
            customer_order.append([item_id, item_quantity])

            if not self.ask_yes_no("Do you want to order another item?"):
                break
        return customer_order

    def calculate_order_details(self, customer_order):
        # 7. Compute bulk discounts and overall subtotals
        itemized_list = []
        order_subtotal = 0.00

        for order_entry in customer_order:
            item_id = order_entry[0]
            item_quantity = order_entry[1]
            item_name = self.menu[item_id]["name"]
            item_price = self.menu[item_id]["price"]
            item_total = item_price * item_quantity
            discount_note = ""

            if item_quantity >= self.bulk_threshold:
                bulk_discount_amount = item_total * self.bulk_discount_rate
                item_total -= bulk_discount_amount
                discount_note = f"(-{int(self.bulk_discount_rate * 100)}% bulk)"

            order_subtotal += item_total
            itemized_list.append([item_name, item_quantity, item_price, item_total, discount_note])

        big_order_discount_amount = 0.00
        if order_subtotal >= self.big_order_threshold:
            big_order_discount_amount = order_subtotal * self.big_order_discount_rate

        final_total = order_subtotal - big_order_discount_amount

        return {
            "itemized_list": itemized_list,
            "subtotal": order_subtotal,
            "big_order_discount": big_order_discount_amount,
            "final_total": final_total,
        }

    def print_receipt(self, order_details):
        # 8. Print the formal receipt summary
        itemized_list = order_details["itemized_list"]
        current_datetime = datetime.now().strftime("%B %d, %Y  %I:%M %p")

        print("\n")
        print("*" * 50)
        print(f"{self.restaurant_name:^50}")
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
            discount_label = f"Loyalty Discount (-{int(self.big_order_discount_rate * 100)}%):"
            print(f"{discount_label:<35}{-order_details['big_order_discount']:>15.2f}")

        print("=" * 50)
        print(f"{'TOTAL:':<35}{order_details['final_total']:>15.2f}")
        print("=" * 50)
        print(f"{'Thank you for ordering with us!':^50}")
        print(f"{'Please come again!':^50}")
        print("*" * 50)

    def run(self):
        # 9. Main control flow that coordinates all methods
        print("Welcome to " + self.restaurant_name + "!\n")
        self.display_menu()

        if not self.ask_yes_no("\nWould you like to place an order?"):
            print("\nNo problem! Have a great day!")
            return

        customer_order = self.take_customer_order()
        order_details = self.calculate_order_details(customer_order)
        self.print_receipt(order_details)