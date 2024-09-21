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
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    return sorted_products


def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")


def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")


def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))


def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item[0][0]} - Quantity: {item[1]}")


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Name: {name}")
    print(f"Email: {email}")
    display_cart(cart)
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")


def validate_name(name):
    parts = name.split()
    if len(parts)!= 2:
        return False
    for part in parts:
        if not part.isalpha():
            return False
    return True


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

    display_categories()
    category_choice = int(input("Select a category by entering the corresponding number: "))
    while category_choice not in range(1, len(products.keys()) + 1):
        print("Invalid category choice. Please enter a correct number.")
        category_choice = int(input("Select a category by entering the corresponding number: "))

    category_names = list(products.keys())
    selected_category = category_names[category_choice - 1]
    display_products(products[selected_category])

    while True:
        option = int(input("Options:\n1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping\n"))
        if option == 1:
            product_number = int(input("Enter the number corresponding to the product you want to buy: "))
            if product_number not in range(1, len(products[selected_category]) + 1):
                print("Invalid product choice. Please enter a correct number.")
                continue
            quantity = int(input("Enter the quantity you want to buy: "))
            add_to_cart(cart, products[selected_category][product_number - 1], quantity)
        elif option == 2:
            sort_order = int(input("Select sorting order:\n1. Ascending\n2. Descending\n"))
            sorted_products = display_sorted_products(products[selected_category], sort_order)
            products[selected_category] = sorted_products
            display_products(sorted_products)
        elif option == 3:
            display_categories()
            category_choice = int(input("Select a category by entering the corresponding number: "))
            while category_choice not in range(1, len(products.keys()) + 1):
                print("Invalid category choice. Please enter a correct number.")
                category_choice = int(input("Select a category by entering the corresponding number: "))
            selected_category = category_names[category_choice - 1]
            display_products(products[selected_category])
        elif option == 4:
            if not cart:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
            else:
                display_cart(cart)
                total_cost = sum(product[1] * quantity for product, quantity in cart)
                address = input("Please enter your delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            break


cart = []

if __name__ == "__main__":
    main()