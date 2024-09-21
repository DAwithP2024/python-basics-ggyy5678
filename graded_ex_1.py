# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)


def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")


def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    choice = input("Select a category by entering the corresponding number: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(products):
            return index
        else:
            return None
    except ValueError:
        return None


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))


def display_cart(cart):
    total_cost = 0
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your cart contains:")
        for item in cart:
            cost = item[1] * item[2]
            print(f"{item[0]} - ${item[1]} x {item[2]} = ${cost}")
            total_cost += cost
        print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item in cart:
        cost = item[1] * item[2]
        print(f"{item[2]} x {item[0]} - ${item[1]} = ${cost}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")


def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)


def validate_email(email):
    return '@' in email


def main():
    name = input("Please enter your name (first name and last name): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name with first name and last name containing only alphabets.")
        name = input("Please enter your name (first name and last name): ")

    email = input("Please enter your email address: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email address with '@' symbol.")
        email = input("Please enter your email address: ")

    category_index = display_categories()
    while category_index is None:
        print("Invalid category choice. Please enter a correct number.")
        category_index = display_categories()

    category_names = list(products.keys())
    selected_category = category_names[category_index]
    display_products(products[selected_category])

    cart = []
    while True:
        option = input("Options:\n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping\n")
        if option == "1":
            product_number = input("Enter the number corresponding to the product you want to buy: ")
            if not product_number.isdigit() or int(product_number) not in range(1, len(products[selected_category]) + 1):
                print("Invalid product choice. Please enter a correct number.")
                continue
            quantity = input("Enter the quantity you want to buy: ")
            while not quantity.isdigit() or int(quantity) <= 0:
                print("Invalid quantity. Please enter a positive integer.")
                quantity = input("Enter the quantity you want to buy: ")
            add_to_cart(cart, products[selected_category][int(product_number) - 1], int(quantity))
        elif option == "2":
            sort_order = input("Select sorting order:\n1. Ascending\n2. Descending\n")
            while sort_order not in ["1", "2"]:
                print("Invalid sorting choice. Please enter 1 for ascending or 2 for descending.")
                sort_order = input("Select sorting order:\n1. Ascending\n2. Descending\n")
            sorted_products = display_sorted_products(products[selected_category], sort_order)
            products[selected_category] = sorted_products
            display_products(sorted_products)
        elif option == "3":
            category_index = display_categories()
            while category_index is None:
                print("Invalid category choice. Please enter a correct number.")
                category_index = display_categories()
            selected_category = category_names[category_index]
            display_products(products[selected_category])
        elif option == "4":
            if not cart:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
            else:
                display_cart(cart)
                total_cost = sum(item[1] * item[2] for item in cart)
                address = input("Please enter your delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            break


if __name__ == "__main__":
    main()