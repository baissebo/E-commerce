class Category:
    total_categories = 0
    unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.unique_products += 1

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    @property
    def formatted_products(self):
        formatted_products = []
        for product in self.__products:
            formatted_products.append(
                f"{product.get_product_name()}, {product.get_product_price()} руб. Остаток: {product.get_product_quantity()} шт.")
        return formatted_products


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Введена некорректная цена.")
            return
        else:
            if new_price < self._price:
                answer = input("Вы понижаете цену товара. Хотите ли вы продолжить? (y/n): ")
                if answer != "y":
                    return
        self._price = new_price

    def get_product_name(self):
        return self.name

    def get_product_description(self):
        return self.description

    def get_product_quantity(self):
        return self.quantity

    @classmethod
    def create_product(cls, product_data, products):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']

        for product in products:
            if product.get_product_name() == name:
                product.price = max(product.price, price)
                product.quantity += quantity
                return product

        return cls(name, description, price, quantity)
