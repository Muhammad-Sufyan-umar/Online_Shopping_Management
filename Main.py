class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_product(self):
        return f"Product Name: {self.name}, Price: Rs.{self.price}, Stock: {self.stock}"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()

    def __str__(self):
        return f"Customer Name: {self.name}, Email: {self.email}"


class Cart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > product.stock:
            print(f"Only {product.stock} items available in stock.")
            return

        self.cart.append((product, quantity))
        product.stock -= quantity

        print(f"{quantity} X {product.name} added to cart.")

    def remove_from_cart(self, product):

        for item in self.cart:

            if item[0] == product:
                self.cart.remove(item)
                product.stock += item[1]

                print(f"{item[1]} X {product.name} removed from cart.")
                return

        print(f"{product.name} not found in cart.")

    def show_cart(self):

        print("\n----- Cart -----")

        if not self.cart:
            print("Cart is Empty")
            return

        total = 0

        for product, quantity in self.cart:

            print(
                f"{product.name} | "
                f"Quantity: {quantity} | "
                f"Price: Rs.{product.price}"
            )

            total += product.price * quantity

        print(f"Total Price: Rs.{total}")


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.status = "Pending"

    def place_order(self):

        if not self.customer.cart.cart:
            print("Cart is empty. Cannot place order.")
            return

        self.status = "Placed"

        print(f"Order placed for {self.customer.name}.")

        self.customer.cart.cart.clear()

    def show_order_status(self):
        print(f"Order Status: {self.status}")


# Products

products = [
    Product("Laptop", 80000, 5),
    Product("Mouse", 1500, 10),
    Product("Keyboard", 3000, 8),
    Product("Headphones", 5000, 6)
]


# Customer

customer = Customer(
    "Sufyan",
    "sufyan@example.com"
)

print(customer)


# Available Products

print("\n----- Available Products -----")

for product in products:
    print(product.show_product())


# Add products to cart

customer.cart.add_to_cart(products[0], 1)
customer.cart.add_to_cart(products[1], 2)
customer.cart.add_to_cart(products[3], 1)


# Show cart

customer.cart.show_cart()


# Place order

order = Order(customer)

order.place_order()

order.show_order_status()


# Show cart after order

print("\nCart after order:")
customer.cart.show_cart()