class Product:
    def __init__(self,name ,price):
        self.name=name
        self.price=price

    def show_product(self):
        print(f"Product Name: {self.name}, Price : {self.price}")

    class Customer:
        def __init__(self,name):
            self.name=name
            self.cart=[]

        def add_to_cart(self,product):
            self.cart.append(product)
            print(f"{product.name} added to cart.")

        def show_cart(self):
            print("\n-----Cart-----")

            if not self.cart:
                print("Cart is Empty")
                return

            total=0

            for product in self.cart:
                product.show_product()
                total+=product.price
            print(f"Total Price: {total}")

class Order:
    def __init__(self,customer):
        self.customer=customer
        self.status="Pending"

    def place_order(self):
        if not self.customer.cart:
            print("Cart is empty. Cannot place order.")
            return

        self.status="Placed"
        print(f"Order placed for {self.customer.name}.")
        self.customer.cart.clear()

    def show_order_status(self):
        print(f"Order Status: {self.status}")

laptop = Product("Laptop", 1000)
phone = Product("Phone", 500)
keyboard = Product("Keyboard", 10000)


