from src.prod_cat import Category, Product
from src.Smart_Grass import LawnGrass, Smartphone
from src.base_prod import order

if __name__ == "__main__":
    prod_list = []
    # создадим пару продуктов
    xiao = Product("Xiaomi Redmi Note 12", "ноут норм", 100, 2)
    # print(xiao.__annotations__)
    realme = Product("Realme NEO GT 5", "нео норм", 150, 15)
    grass = LawnGrass("russia", 1, "blue", "северное сияние", "5+", 199, 1)
    realme_smart = Smartphone(
        "высокая", "realme", 1024, "blue", "realme ultra pro max se 10", "bad", 10, 1500
    )
    # создадим категорию смартфонов, пока пустую
    phones_category = Category("Телефоны", "Сюда будем добавлять смартфоны", [])
    phones_category2 = Category("Телефоны2", "Сюда будем добавлять смартфоны", [])
    print(phones_category.av_price())
    # добавляем экземпляры продуктов
    phones_category.add_product(xiao)
    phones_category.add_product(realme)
    phones_category.add_product(realme_smart)
    print(phones_category.av_price())
    buy = order("Xiaomi Redmi Note 12", 2)
    print(buy.pirchase(xiao))
    # вызываем геттер списка строковых представлений продуктов и смотрим, что всё распечатывается
    print(realme_smart)
    print(grass)
    print(phones_category.show_prod)
    print(phones_category)
    print(xiao + realme)

    # готовим данные
    product_info = {
        "name": "Poco X6",
        "description": "поко норм",
        "price": 120,
        "quantity": 2,
    }
    # создаём из словаря продукт
    pocophone = Product.new_product(product_info)
    # пробуем установить отрицательную цену, видим сообщение, программа продолжает работать
    pocophone.price = -5
    # выводим его цену, должны увидеть 120
    print(pocophone.price)
