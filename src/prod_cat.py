import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


class Category:
    name: str
    description: str
    products: list
    number_of_products = 0
    number_of_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.number_of_products += len(products)

    @staticmethod
    def counter_cat():
        Category.number_of_categories += 1

    @staticmethod
    def get_count():
        return Category.number_of_categories

    # def add_product(self, prod):
    #     added_list = {}
    #     keys = ["name", "description", "price", "quantity"]
    #     items = [prod.name, prod.description, prod.show_price, prod.quantity]
    #     for i in range(len(keys)):
    #         added_list[keys[i]] = items[i]
    #     self.__products.append(added_list)
    #     self.number_of_products += 1
    def add_product(self, product):
        self.number_of_products += 1
        self.__products.append(product)

    @property
    def show_prod(self):
        result = []
        for prods in self.__products:
            result.append(
                f'{prods.name}, {prods.price} руб. Остаток: {prods.quantity} шт.'
            )
            # result.append(prods)
        return result

    def display_details(self):
        print("Название категории:", self.name)
        print("Описание категории:", self.description)
        for prod in self.show_prod:
            print(prod)


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if self.__price <= 0 or value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif self.__price > value:
            confirmation = input(
                "Цена товара понижается. Вы подтверждаете изменение цены? (y/n)\n"
            )
            if confirmation == "y":
                self.__price = value
            else:
                print("Изменение цены отменено")

    @classmethod
    def new_product(cls, product_dict):
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )
    # def new_product(cls, product_dict):
    #     """Создаёт новый продукт."""
    #     flag = True
    #     for prods in prod_list:
    #         # print(prods.__price)
    #         # print(product_dict["price"])
    #         if prods.name == product_dict["name"]:
    #             flag = False
    #             prods.quantity += product_dict["quantity"]
    #             if product_dict["__price"] > prods.__price:
    #                 prods.__price = product_dict["__price"]
    #     if flag == True:
    #         prod_list.append(
    #             cls(
    #                 product_dict["name"],
    #                 product_dict["description"],
    #                 product_dict["__price"],
    #                 product_dict["quantity"],
    #             )
    #         )
    #     return cls(
    #         product_dict["name"],
    #         product_dict["description"],
    #         product_dict["__price"],
    #         product_dict["quantity"],
    #     )

    def display_details(self):
        print("Название продукта:", self.name)
        print("Описание продукта:", self.description)
        print("Цена продукта:", self.__price)
        print("Количество продукта:", self.quantity)


def prodlist_path(path: str) -> list[dict]:
    """Функция для JSON файла"""
    result = []
    with open(path, encoding="utf8") as json_file:
        result = json.load(json_file)
    return result


if __name__ == "__main__":
    prod_list = []
    cat_list = []
    path_to_json = os.path.join(
        os.path.dirname(__file__), "..", "data", "products.json"
    )
    prod_full = prodlist_path(path_to_json)
    # print(prod_full)
    for item in prod_full:
        category = Category(item["name"], item["description"], [])
        # print(item["products"])
        for items in item["products"]:
            # print(items["name"])
            prod_curr = Product(
                items["name"],
                items["description"],
                items["price"],
                items["quantity"],
            )

            category.add_product(prod_curr)
            prod_list.append(prod_curr)
        cat_list.append(category)
    # print(cat_list[1].show_prod[0].name)
    # for category in catList:
    #     category.display_details()
    # print(prodList)
    # print(catList)
    # product1 = Product.new_product(
    #     {
    #         "name": "Xiaomi Redmi Note 112",
    #         "description": "ноут норм",
    #         "__price": 100,
    #         "quantity": 222,
    #     }
    # )
    # # print(prodList)
    # # print(product1)
    # print(product1.name, product1.description, product1.show_price, product1.quantity)
    # # print(prodList[2].show_price)
    # cat_add = input("Введите категорию\n")
    # for obj in catList:
    #     obj.counter_cat()
    #     if obj.name == cat_add:
    #         name_add = input("Введите имя товара\n")
    #         description_add = input("Введите описание товара\n")
    #         price_add = input("Введите цену\n")
    #         quantity_add = input("Введите количество\n")
    #         obj.add_product(
    #             Product(name_add, description_add, float(price_add), int(quantity_add))
    #         )
    #     else:
    #         print("такой категории нет")
    #
    #     print(obj.name)
    #     print(obj.description)
    #     print(obj.show_prod)
    #     print(obj.number_of_products)
    # #
    # print(Category.get_count())
    # print(prod_List[4].name)
    # prod_List[4].show_price = 1000
    # prod_List[4].show_price = 1000
    # print(prod_List[4].show_price)
    # for obj in prod_List:
    #     print(obj.name)
    #     print(obj.description)
    #     print(obj.show_price)
    #     print(obj.quantity)
    print(cat_list[0].show_prod)
