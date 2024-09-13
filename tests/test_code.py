import pytest
from src.prod_cat import Product, Category, prodlist_path
from src.Smart_Grass import Smartphone, LawnGrass
from src.base_prod import BaseProduct, Mixin
import os


@pytest.fixture
def json_file():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]


@pytest.fixture
def pathjson():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_json = os.path.join(
        os.path.dirname(__file__), "..", "data", "products.json"
    )
    return path_to_json


@pytest.fixture()
def pocophone():
    product_info = {
        "name": "Poco X6",
        "description": "поко норм",
        "price": 120,
        "quantity": 5,
    }
    pocophone = Product.new_product(product_info)
    return pocophone


@pytest.fixture
def xiao():
    return Product("Xiaomi Redmi Note 12", "ноут норм", 100, 222)


@pytest.fixture
def realme():
    return Product("Realme NEO GT 5", "нео норм", 150, 15)


@pytest.fixture
def products():
    return Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def categories(products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [products],
    )


@pytest.fixture()
def smart_fixture():
    return Smartphone(
        "высокая", "realme", 1024, "blue", "realme ultra pro max se 10", "bad", 10, 1500
    )


@pytest.fixture()
def grass_fixture():
    return LawnGrass("russia", 1, "blue", "северное сияние", "5+", 199, 999)


def test_init_prod(products):
    assert products.name == "Samsung Galaxy C23 Ultra"
    assert products.description == "256GB, Серый цвет, 200MP камера"
    assert products.price == 180000.0
    assert products.quantity == 5


def test_init_cat(categories):
    assert categories.name == "Смартфоны"
    assert (
        categories.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert categories.show_prod == [
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.",
    ]
    assert categories.number_of_products == 1
    assert categories.number_of_categories == 0


def test_add_product(categories, xiao):
    categories.add_product(xiao)
    assert categories.show_prod == [
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Xiaomi Redmi Note 12, 100 руб. Остаток: 222 шт.",
    ]
    with pytest.raises(TypeError):
        categories.add_product(categories)


def test_price(pocophone):
    assert pocophone.price == 120


def test_prodlist(pathjson, json_file):
    assert prodlist_path(pathjson) == json_file


def test_add(xiao, realme, grass_fixture):
    assert realme + xiao == 24450
    with pytest.raises(TypeError):
        realme + grass_fixture


def test_mixin():
    assert Mixin.__class__.__name__ == "type"
