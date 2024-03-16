from src.category import Category
from src.product import Product
from src.utils import load_data
import pytest


@pytest.fixture
def category():
    data = load_data()
    category_data = data[1]

    category_name = category_data["name"]
    category_description = category_data["description"]
    category_products = category_data["products"]

    products = []

    for product_data in category_products:
        product_name = product_data["name"]
        product_description = product_data["description"]
        product_price = product_data["price"]
        product_quantity = product_data["quantity"]

        product = Product(product_name, product_description, product_price, product_quantity)
        products.append(product)

    return Category(category_name, category_description, products)


def test_category_init(category):
    assert category.name == 'Телевизоры'
    assert category.description == ('Современный телевизор, который позволяет наслаждаться просмотром, '
                                    'станет вашим другом и помощником')
    assert len(category.get_products()) == 1
    assert Category.total_categories == 1
    assert Category.unique_products == 1


def test_get_name(category):
    assert category.get_name() == 'Телевизоры'


def test_get_description(category):
    assert category.get_description() == ('Современный телевизор, который позволяет наслаждаться просмотром, '
                                          'станет вашим другом и помощником')


def test_get_products(category):
    assert len(category.get_products()) == 1
