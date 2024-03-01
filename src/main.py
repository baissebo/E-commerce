class Category:
    total_categories = 0
    unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories += 1
        Category.unique_products += 1

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.products


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_price(self):
        return self.price

    def get_product_quantity(self):
        return self.quantity
