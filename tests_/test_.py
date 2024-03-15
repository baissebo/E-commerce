from src.main import Category, Product, Smartphone, LawnGrass
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


@pytest.mark.parametrize("name, description, price, quantity, performance, model, storage, color", [
    ("iPhone 12", "iPhone Apple", 999.99, 10, 3.0, "12 Pro Max", 256, "Pacific Blue"),
    ("Samsung Galaxy S21", "Samsung", 899.99, 5, 2.8, "S21 Ultra", 512, "Phantom Black"),
])
def test_smartphone_init(name, description, price, quantity, performance, model, storage, color):
    smartphone = Smartphone(name, description, price, quantity, performance, model, storage, color)
    assert smartphone.name == name
    assert smartphone.description == description
    assert smartphone.price == price
    assert smartphone.quantity == quantity
    assert smartphone.performance == performance
    assert smartphone.model == model
    assert smartphone.storage == storage
    assert smartphone.color == color


@pytest.mark.parametrize("name, description, price, quantity, country, growth_period, color", [
    ("Green Grass", "Healthy and lush green grass", 9.99, 100, "USA", "Spring/Summer", "Green"),
    ("Fresh Lawn", "High-quality beautiful lawn", 7.99, 50, "UK", "Summer", "Blue"),
])
def test_lawn_grass_init(name, description, price, quantity, country, growth_period, color):
    lawn_grass = LawnGrass(name, description, price, quantity, country, growth_period, color)
    assert lawn_grass.name == name
    assert lawn_grass.description == description
    assert lawn_grass.price == price
    assert lawn_grass.quantity == quantity
    assert lawn_grass.country == country
    assert lawn_grass.growth_period == growth_period
    assert lawn_grass.color == color
