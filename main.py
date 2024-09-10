from src.prod_cat import Product, Category, prodlist_path

if __name__ == "__main__":
    prod_list = []
    # создадим пару продуктов
    xiao = Product("Xiaomi Redmi Note 12", "ноут норм", 100, 222)
    realme = Product("Realme NEO GT 5", "нео норм", 150, 15)
    # создадим категорию смартфонов, пока пустую
    phones_category = Category("Телефоны", "Сюда будем добавлять смартфоны", [])
    # добавляем экземпляры продуктов
    phones_category.add_product(xiao)
    phones_category.add_product(realme)
    # вызываем геттер списка строковых представлений продуктов и смотрим, что всё распечатывается

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
