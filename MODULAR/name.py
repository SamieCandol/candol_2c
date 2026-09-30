RESTAURANT_NAME = "HARAYA RESTAURANT "

def get_restaurant_name():
    return RESTAURANT_NAME

def ask_yes_no(question):
    while True:
        answer = input(f"{question} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  >> Invalid input. Please type 'y' or 'n'.")