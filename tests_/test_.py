from src.main import Category, Product
import pytest
from src.utils import load_data


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


@pytest.fixture
def product():
    data = load_data()
    category_data = data[1]
    product_data = category_data["products"][0]

    product_name = product_data["name"]
    product_description = product_data["description"]
    product_price = product_data["price"]
    product_quantity = product_data["quantity"]

    return Product(product_name, product_description, product_price, product_quantity)


def test_category_init(category):
    assert category.name == 'Телевизоры'
    assert category.description == 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'
    assert len(category.products) == 1
    assert Category.total_categories == 1
    assert Category.unique_products == 1


def test_get_name(category):
    assert category.get_name() == 'Телевизоры'


def test_get_description(category):
    assert category.get_description() == 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником'


def test_get_products(category):
    assert len(category.get_products()) == 1


def test_product_init(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_product_name(product):
    assert product.get_product_name() == "55\" QLED 4K"


def test_product_description(product):
    assert product.get_product_description() == "Фоновая подсветка"


def test_product_price(product):
    assert product.get_product_price() == 123000.0


def test_product_quantity(product):
    assert product.get_product_quantity() == 7
