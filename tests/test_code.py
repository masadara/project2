import pytest
from src.main import Product, Category, prodlist
import os


@pytest.fixture
def JSON_file():
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
def pathJSON():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_to_json = os.path.join(
        os.path.dirname(__file__), "..", "data", "products.json"
    )
    return path_to_json


@pytest.fixture
def Products():
    return Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def Categories():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [
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
    )


def test_init_prod(Products):
    assert Products.name == "Samsung Galaxy C23 Ultra"
    assert Products.description == "256GB, Серый цвет, 200MP камера"
    assert Products.price == 180000.0
    assert Products.quantity == 5


def test_init_cat(Categories):
    assert Categories.name == "Смартфоны"
    assert (
        Categories.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Categories.products == [
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
    ]
    assert Categories.number_of_products == 3
    assert Categories.number_of_categories == 1


def test_prodlist(pathJSON, JSON_file):
    assert prodlist(pathJSON) == JSON_file
