orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
    ]

def format_orders():
    for index, order in enumerate(orders):
        customer, product, quantity = order
        print("-" * 50)
        print(f"Order #{index + 1}\nCustomer: {customer}\nProduct: {product}\nQuantity: {quantity}")
    return "-" * 50

print(format_orders())