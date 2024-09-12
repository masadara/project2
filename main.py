from src.prod_cat import Category, Product
from src.Smart_Grass import LawnGrass, Smartphone

if __name__ == "__main__":
    prod_list = []
    # создадим пару продуктов
    xiao = Product("Xiaomi Redmi Note 12", "ноут норм", 100, 222)
    realme = Product("Realme NEO GT 5", "нео норм", 150, 15)
    grass = LawnGrass("russia", 1, "blue", "северное сияние", "5+", 199, 999)
    realme_smart = Smartphone(
        "высокая", "realme", 1024, "blue", "realme ultra pro max se 10", "bad", 10, 1500
    )
    # создадим категорию смартфонов, пока пустую
    phones_category = Category("Телефоны", "Сюда будем добавлять смартфоны", [])
    phones_category2 = Category("Телефоны2", "Сюда будем добавлять смартфоны", [])
    # добавляем экземпляры продуктов
    phones_category.add_product(xiao)
    phones_category.add_product(realme)
    phones_category.add_product(realme_smart)
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
        "quantity": 5,
    }
    # создаём из словаря продукт
    pocophone = Product.new_product(product_info)
    # пробуем установить отрицательную цену, видим сообщение, программа продолжает работать
    pocophone.price = -5
    # выводим его цену, должны увидеть 120
    print(pocophone.price)
