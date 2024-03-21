from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def get_product_name(self):
        pass

    @abstractmethod
    def get_product_description(self):
        pass

    @abstractmethod
    def get_product_quantity(self):
        pass

    @abstractmethod
    def get_product_info(self):
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, product_data, products):
        pass


class CreationInfoMixin:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)
        print(self)

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join([f'{attr}={getattr(self, attr)}' for attr in self.__dict__])
        return f"{class_name}({attributes})"


class Product(CreationInfoMixin, BaseProduct):

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

    def get_product_info(self):
        pass

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

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError

        total = (self.price * self.quantity) + (other.price * other.quantity)
        return total

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __len__(self):
        return self.quantity


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, performance: float, model: str,
                 storage: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage = storage
        self.color = color

    def get_product_info(self):
        return f"{self.name}, {self.model}, {self.description}, Производительность: {self.performance} ГГц, " \
               f"Цвет: {self.color}, Цена: {self.price} руб. Остаток: {self.quantity} шт."


class LawnGrass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, growth_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.growth_period = growth_period
        self.color = color

    def get_product_info(self):
        return f"{self.name}, {self.description}, Период прорастания: {self.growth_period}, Цвет: {self.color}, " \
               f"Цена: {self.price} руб. Остаток: {self.quantity} шт."
