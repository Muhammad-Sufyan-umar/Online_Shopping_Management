# 🛒 Online Shopping System

A simple **Online Shopping System** built in Python using **Object-Oriented Programming (OOP)** concepts.

The project allows customers to view products, add products to a cart, remove products, calculate the total price, and place orders.

## 🚀 Features

* Display available products
* Show product name, price, and stock
* Create customer with name and email
* Add products to cart
* Validate product quantity
* Check available stock
* Automatically update stock when adding to cart
* Remove products from cart
* Restore stock when a product is removed
* Calculate total cart price
* Place an order
* Show order status
* Clear cart after successful order

## 🧱 Classes Used

### 1. Product

Represents a product available in the store.

**Attributes:**

* `name`
* `price`
* `stock`

**Method:**

* `show_product()`

### 2. Customer

Represents a customer of the shopping system.

**Attributes:**

* `name`
* `email`
* `cart`

### 3. Cart

Manages the products selected by the customer.

**Methods:**

* `add_to_cart()`
* `remove_from_cart()`
* `show_cart()`

### 4. Order

Handles the customer's order.

**Attributes:**

* `customer`
* `status`

**Methods:**

* `place_order()`
* `show_order_status()`

## 💡 OOP Concepts Used

This project demonstrates several important OOP concepts:

* **Classes and Objects**
* **Constructors (`__init__`)**
* **Instance Attributes**
* **Instance Methods**
* **Object Composition**
* **Encapsulation**
* **`__str__()` Method**

### Object Composition

The `Customer` class contains a `Cart` object:

```python
self.cart = Cart()
```

This means each customer has their own shopping cart.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python main.py
```

## 📌 Example Products

The system currently contains:

| Product    |     Price | Stock |
| ---------- | --------: | ----: |
| Laptop     | Rs.80,000 |     5 |
| Mouse      |  Rs.1,500 |    10 |
| Keyboard   |  Rs.3,000 |     8 |
| Headphones |  Rs.5,000 |     6 |

## 🧮 Example Cart

The customer adds:

* 1 × Laptop
* 2 × Mouse
* 1 × Headphones

The total price is:

**Rs. 88,000**

## 📚 Purpose

This project was created for practicing **Python OOP concepts** and understanding how different classes can work together to build a small real-world application.

## 🔮 Future Improvements

Possible improvements include:

* Product search
* Product categories
* Multiple customers
* User login/signup
* Discount system
* Payment system
* Order history
* Order cancellation
* File/database storage
* Interactive menu-based system

## 👨‍💻 Author

**Sufyan**

Built with ❤️ using **Python**.

