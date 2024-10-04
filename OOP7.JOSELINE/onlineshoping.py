class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")

class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} {product.product_name}(s) to cart.")
        else:
            print(f"Not enough {product.product_name}(s) in stock.")

    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"Removed {item[1]} {product.product_name}(s) from cart.")
                return
        print(f"{product.product_name} not found in cart.")

    def display_cart(self):
        print("Cart Contents:")
        for item in self.items:
            print(f"  {item[0].product_name} x {item[1]}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total

# Creating Product objects
product1 = Product("Apple Watch", 203.86, 4)
product2 = Product("Samsung TV", 454.86, 2)
product3 = Product("Nike Shoes", 761.86, 5)

# Create ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Perform operations on cart1
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart1.remove_from_cart(product1)

# Perform operations on cart2
cart2.add_to_cart(product3, 3)
cart2.add_to_cart(product2, 2)

# Display cart contents and calculate total
print("Cart 1:")
cart1.display_cart()
print(f"Total: ${cart1.calculate_total():.2f}")

print("\nCart 2:")
cart2.display_cart()
print(f"Total: ${cart2.calculate_total():.2f}")