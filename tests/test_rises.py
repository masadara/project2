import pytest
from src.prod_cat import Product, Category


@pytest.fixture
def xiao_zero():
    return Product("Xiaomi Redmi Note 12", "ноут норм", 100, 222)

@pytest.fixture
def cat_zero():
    return Category("Телефоны", "Сюда будем добавлять смартфоны", [])

def test_zero_quantity(xiao_zero):
    with pytest.raises(ValueError):
        Product("Xiaomi Redmi Note 12", "ноут норм", 100, 0)

def test_zero_products(cat_zero):
    assert Category("Телефоны", "Сюда будем добавлять смартфоны", []).av_price() == 0
