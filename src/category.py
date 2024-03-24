from src.product import Product, CreationInfoMixin

from abc import ABC, abstractmethod


class ZeroQuantityException(Exception):
    """
      Исключение, которое возникает при попытке добавить товар с нулевым количеством.
      """

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен."):
        self.message = message
        super().__init__(self.message)


class OrderItem(ABC):
    """
     Абстрактный базовый класс для элементов заказа.
     """

    @abstractmethod
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def get_total_cost(self):
        pass


class Order(OrderItem):
    """
      Класс, представляющий заказ.
      """

    def __init__(self, product, quantity):
        super().__init__(product, quantity)
        self.items = []

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def get_total_cost(self):
        return self.product.price * self.quantity

    def add_item(self, item):
        """
        Добавление товара в заказ
        :param item: объект товара для добавления
        """

        try:
            if item.get_quantity() == 0:
                raise ZeroQuantityException()
        except ZeroQuantityException as e:
            print(e)
        else:
            self.items.append(item)
            print("Товар успешно добавлен в заказ")
        finally:
            print("Обработка добавления товара завершена")


class CategoryIterator:
    """
       Итератор для категории товаров.
       """

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


class Category(CreationInfoMixin, OrderItem):
    """
        Класс, представляющий категорию товаров.
        """

    total_categories = 0
    unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.unique_products += len(products)
        super().__init__()

    def calc_average_price(self):
        """
            Вычисление средней цены товаров в категории.
            """

        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
        except ZeroDivisionError:
            average_price = 0
        return average_price

    def get_total_cost(self):
        return self.product.price * self.quantity

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_products(self):
        return self.__products

    def add_product(self, product):
        """
        Добавление товара в категорию
        :param product: объект товара для добавления
        """

        try:
            if product.get_product_quantity() == 0:
                raise ZeroQuantityException()
        except ZeroQuantityException as e:
            print(e)
        else:
            self.__products.append(product)
            print("Товар успешно добавлен в категорию")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def formatted_products(self):
        """
           Получение отформатированной информации о товарах в категории.
           """

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
