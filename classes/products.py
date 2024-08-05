# 1. Базовый класс Product и производные классы для различных типов продуктов
from abc import ABC, abstractmethod

class Product(ABC):
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Продукт: {self.name}, Цена: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."


class Household_chemicals(Product):
    """
    Класс, представляющий бытовую химию, наследующий класс Product.
    """
    def __init__(self, name, price, product_release_form):
        super().__init__(name, price)
        self.product_release_form = product_release_form
    
    @abstractmethod
    def get_specific_details(self):
        pass



    def get_details(self):
        return f"Бытовая химия: {self.name}, Цена: {self.price} руб., {self.get_specific_details()}"
    
    
class WashingPowder(Household_chemicals):
    def __init__(self, name, price, weight):
        super().__init__(name, price, product_release_form = "Порошок")
        self.weight = weight
        
    def get_specific_details(self):
        return f"Вес: {self.weight} г."
    
    
class CleaningGel(Household_chemicals):
    def __init__(self, name, price, volume):
        super().__init__(name, price, product_release_form = "Гель")
        self.volume = volume
        
    def get_specific_details(self):
        return f"Объем: {self.volume} мл."