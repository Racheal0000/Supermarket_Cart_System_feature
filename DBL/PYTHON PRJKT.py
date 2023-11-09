class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: ugx{self.price}, Quantity: {self.quantity}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        print(f"{self.name}'s Cart:")
        for product in self.cart:
            product.display_info()

    def checkout(self):
        total_price = sum(product.price for product in self.cart)
        print(f"Total Price: ugx{total_price}")
        return total_price


class Supermarket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Available Products:")
        for product in self.products:
            product.display_info()



# Create products
product1 = Product("Apple", 500, 8)
product2 = Product("Banana", 300, 10)
product3 = Product("Orange", 500, 15)

# Create a supermarket and add products
supermarket = Supermarket()
supermarket.add_product(product1)
supermarket.add_product(product2)
supermarket.add_product(product3)

# Create a customer
customer = Customer("Alice")

# Customer adds products to cart
customer.add_to_cart(product1)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

# View cart
customer.view_cart()

# Customer checks out
total_price = customer.checkout()

# List available products in the supermarket
supermarket.list_products()
