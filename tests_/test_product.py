from src.product import Product, Smartphone, LawnGrass
from src.utils import load_data
import pytest


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
    assert product._price == 123000.0


def test_product_quantity(product):
    assert product.get_product_quantity() == 7


@pytest.fixture
def smartphone_data():
    return Smartphone("iPhone 12", "iPhone Apple", 999.99, 10, 3.0, "12 Pro Max", 256, "Pacific Blue")


def test_smartphone_init(smartphone_data):
    assert smartphone_data.name == "iPhone 12"
    assert smartphone_data.description == "iPhone Apple"
    assert smartphone_data.price == 999.99
    assert smartphone_data.quantity == 10
    assert smartphone_data.performance == 3.0
    assert smartphone_data.model == "12 Pro Max"
    assert smartphone_data.storage == 256
    assert smartphone_data.color == "Pacific Blue"


@pytest.fixture
def lawn_grass_data():
    return LawnGrass("Green Grass", "Healthy and lush green grass", 9.99, 100, "USA", "Spring/Summer", "Green")


def test_lawn_grass_init(lawn_grass_data):
    assert lawn_grass_data.name == "Green Grass"
    assert lawn_grass_data.description == "Healthy and lush green grass"
    assert lawn_grass_data.price == 9.99
    assert lawn_grass_data.quantity == 100
    assert lawn_grass_data.country == "USA"
    assert lawn_grass_data.growth_period == "Spring/Summer"
    assert lawn_grass_data.color == "Green"
