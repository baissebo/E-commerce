from src.product import Product

from abc import ABC, abstractmethod


class OrderItem(ABC):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def get_total_cost(self):
        pass


class Order(OrderItem):
    def __init__(self, product, quantity):
        super().__init__(product, quantity)

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def get_total_cost(self):
        return self.product.price * self.quantity


class CategoryIterator:
    def __init__(self, category):
        self.category = category
        self.products = category.get_products()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            current_product = self.products[self.index]
            self.index += 1
            return current_product
        else:
            raise StopIteration


class Category(OrderItem):
    total_categories = 0
    unique_products = 0

    def __init__(self, name: str, description: str, products: list, quantity):
        self.name = name
        self.description = description
        self.__products = products
        self.quantity = quantity
        super().__init__(products, quantity)

        Category.total_categories += 1
        Category.unique_products += 1

    def get_total_cost(self):
        return self.product.price * self.quantity

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.__products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError

        self.__products.append(product)

    @property
    def formatted_products(self):
        formatted_products = []
        for product in self.__products:
            formatted_products.append(
                f"{product.get_product_name()}, {product.get_product_price()} руб. "
                f"Остаток: {product.get_product_quantity()} шт.")
        return formatted_products

    def __str__(self):
        num_products = sum(product.get_product_quantity() for product in self.__products)
        return f"{self.name}, количество продуктов: {num_products} шт."

    def __len__(self):
        return sum(product.get_product_quantity() for product in self.__products)

    def __iter__(self):
        return CategoryIterator(self)
