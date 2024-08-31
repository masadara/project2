import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    number_of_products = 0
    number_of_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.number_of_categories += 1
        self.number_of_products += len(products)


def prodlist(path: str) -> list[dict]:
    result = []
    with open(path, encoding="utf8") as json_file:
        result = json.load(json_file)
    return result


if __name__ == "__main__":
    prod1 = Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    prodList = []
    catList = []

    path_to_json = os.path.join(os.path.dirname(__file__), "data", "products.json")
    prod_full = prodlist(path_to_json)
    print(prod_full)
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
    for obj in prodList:
        print(obj.name)
        print(obj.description)
        print(obj.price)
        print(obj.quantity)

    for obj in catList:
        print(obj.name)
        print(obj.description)
        print(obj.products)
        print(obj.number_of_products)
        print(obj.number_of_categories)
