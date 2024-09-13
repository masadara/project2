from src.prod_cat import Product, Category, prodlist_path
from src.base_prod import Mixin

class Smartphone(Product, Mixin):
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(self, efficiency, model, memory, color, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product, Mixin):
    country: str
    germination_period: int
    color: str

    def __init__(self, country, germination_period, color, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.germination_period = germination_period
        self.country = country
        self.color = color