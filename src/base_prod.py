from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Base_cat_order(ABC):
    def __init__(self):
        pass


class Mixin:

    def __init__(self):
        self.__repr__()
        print(self.__repr__())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class order(Base_cat_order):
    # purchase: cls
    name_purchase: str
    quantity: int

    def __init__(self, name_purchase, quantity):
        self.name_purchase = name_purchase
        self.quantity = quantity
        super().__init__()

    def pirchase(self, prod):
        if self.name_purchase == prod.name and self.quantity <= prod.quantity:
            return f"куплен {self.name_purchase}, в количестве: {self.quantity} на сумму {self.quantity * prod.price}"
        else:
            return "Покупка невозможна"
