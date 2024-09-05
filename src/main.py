import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


class Category:
    name: str
    description: str
    products: list
    number_of_products = 0
    number_of_categories = 0

    def __init__(self, name, description, __products):
        self.name = name
        self.description = description
        self.__products = __products
        self.number_of_products += len(__products)

    @staticmethod
    def counter_cat():
        Category.number_of_categories += 1

    @staticmethod
    def get_count():
        return Category.number_of_categories

    def add_product(self, prod):
        added_list = {}
        keys = ["name", "description", "price", "quantity"]
        items = [prod.name, prod.description, prod.show_price, prod.quantity]
        for i in range(len(keys)):
            added_list[keys[i]] = items[i]
        self.__products.append(added_list)
        self.number_of_products += 1

    @property
    def show_prod(self):
        result = []
        for prods in self.__products:
            result.append(
                f'{prods.get("name")}, {prods.get("price")} руб. Остаток: {prods.get("quantity")} шт.'
            )
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

    def __init__(self, name, description, __price, quantity):
        self.name = name
        self.description = description
        self.__price = __price
        self.quantity = quantity

    @property
    def show_price(self):
        return self.__price

    @show_price.setter
    def show_price(self, value):
        if self.__price <= 0 or value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
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
        """Создаёт новый продукт."""
        flag = True
        for prods in prodList:
            # print(prods.__price)
            # print(product_dict["price"])
            if prods.name == product_dict["name"]:
                flag = False
                prods.quantity += product_dict["quantity"]
                if product_dict["__price"] > prods.__price:
                    prods.__price = product_dict["__price"]
        if flag == True:
            prodList.append(
                cls(
                    product_dict["name"],
                    product_dict["description"],
                    product_dict["__price"],
                    product_dict["quantity"],
                )
            )
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["__price"],
            product_dict["quantity"],
        )

    def display_details(self):
        print("Название продукта:", self.name)
        print("Описание продукта:", self.description)
        print("Цена продукта:", self.__price)
        print("Количество продукта:", self.quantity)


def prodlist(path: str) -> list[dict]:
    """Функция для JSON файла"""
    result = []
    with open(path, encoding="utf8") as json_file:
        result = json.load(json_file)
    return result


if __name__ == "__main__":
    prodList = []
    catList = []
    path_to_json = os.path.join(
        os.path.dirname(__file__), "..", "data", "products.json"
    )
    prod_full = prodlist(path_to_json)
    for item_cat in prod_full:
        catList.append(
            Category(
                item_cat["name"],
                item_cat["description"],
                item_cat["products"],
            )
        )
        for item_prod in item_cat.get("products"):
            prodList.append(
                Product(
                    item_prod["name"],
                    item_prod["description"],
                    item_prod["price"],
                    item_prod["quantity"],
                )
            )
    # for category in catList:
    #     category.display_details()
    # print(prodList)
    # print(catList)
    product1 = Product.new_product(
        {
            "name": "Xiaomi Redmi Note 112",
            "description": "ноут норм",
            "__price": 100,
            "quantity": 222,
        }
    )
    # print(prodList)
    # print(product1)
    print(product1.name, product1.description, product1.show_price, product1.quantity)
    # print(prodList[2].show_price)
    cat_add = input("Введите категорию\n")
    for obj in catList:
        obj.counter_cat()
        if obj.name == cat_add:
            name_add = input("Введите имя товара\n")
            description_add = input("Введите описание товара\n")
            price_add = input("Введите цену\n")
            quantity_add = input("Введите количество\n")
            obj.add_product(
                Product(name_add, description_add, float(price_add), int(quantity_add))
            )
        else:
            print("такой категории нет")

        print(obj.name)
        print(obj.description)
        print(obj.show_prod)
        print(obj.number_of_products)
    #
    print(Category.get_count())
    print(prodList[4].name)
    prodList[4].show_price = 1000
    prodList[4].show_price = 1000
    print(prodList[4].show_price)
    for obj in prodList:
        print(obj.name)
        print(obj.description)
        print(obj.show_price)
        print(obj.quantity)
