class Category:
    total_categories = 0
    unique_products = set()

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1

        for product in products:
            Category.unique_products.add(product)


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


