cart = []

store = {
    "Apple": {"price": 50, "category": "Fruits"},
    "Banana": {"price": 30, "category": "Fruits"},
    "Milk": {"price": 60, "category": "Dairy"},
    "Bread": {"price": 40, "category": "Bakery"},
    "Eggs": {"price": 80, "category": "Dairy"},
}

categories = set()


def show_products():
    print("\n---------- AVAILABLE PRODUCTS ----------")

    for item, details in store.items():
        print(
            f"{item:<10} ₹{details['price']:<5} Category: {details['category']}"
        )


def add_item():
    show_products()

    item = input("\nEnter product name: ").title()

    if item not in store:
        print("Product not found.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid quantity.")
        return

    cart.append(
        {
            "item": item,
            "price": store[item]["price"],
            "quantity": quantity,
        }
    )

    categories.add(store[item]["category"])

    print("Item added successfully.")


def view_cart():

    if not cart:
        print("Your cart is empty.")
        return

    print("\n---------- YOUR CART ----------")

    total = 0

    for product in cart:
        subtotal = product["price"] * product["quantity"]
        total += subtotal

        print(
            f"{product['item']:<10}"
            f"Qty: {product['quantity']:<3}"
            f"Price: ₹{product['price']:<4}"
            f"Subtotal: ₹{subtotal}"
        )

    print(f"\nTotal Bill: ₹{total}")


def remove_item():

    if not cart:
        print("Cart is empty.")
        return

    item = input("Enter product name to remove: ").title()

    for product in cart:
        if product["item"] == item:
            cart.remove(product)
            print("Item removed successfully.")
            return

    print("Item not found in cart.")


def show_categories():

    if not categories:
        print("No categories in cart.")
        return

    print("\nCategories Purchased:")

    for category in categories:
        print(category)


def checkout():

    if not cart:
        print("Cart is empty.")
        return

    total = 0

    print("\n---------- FINAL BILL ----------")

    for product in cart:
        subtotal = product["price"] * product["quantity"]
        total += subtotal

        print(
            f"{product['item']} x {product['quantity']} = ₹{subtotal}"
        )

    print("-----------------------------")
    print(f"Grand Total: ₹{total}")
    print("Thank you for shopping!")

    cart.clear()
    categories.clear()


def menu():

    while True:

        print("""
========== SHOPPING CART ==========
1. Show Products
2. Add Item
3. View Cart
4. Remove Item
5. Show Categories
6. Checkout
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            add_item()

        elif choice == "3":
            view_cart()

        elif choice == "4":
            remove_item()

        elif choice == "5":
            show_categories()

        elif choice == "6":
            checkout()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


menu()
