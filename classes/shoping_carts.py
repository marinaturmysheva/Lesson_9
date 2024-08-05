# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self):
       self.items = []
       self.total_cost = 0
       self.registered_by = ""
        
        

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

#    def get_details(self):
#       """
#       Возвращает детализированную информацию о содержимом корзины и общей стоимости.
#       """
#        details = "Корзина покупок:\n"
#        for item in self.items:
#            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
#        details += f"Общее: {self.get_total()} руб"
#        return details
    
    def get_details(self, customer, admin):
        """
        Возвращает детализированную информацию о содержимом корзины, общей стоимости и участниках покупки.
        """
        # details = f"{customer.get_details()} приобрел:\n"  # информация о покупателе
        # for item in self.items:
        #     details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        # details += f"Общая стоимость: {self.get_total()} руб\n"
        # details += f"Зарегистрировал покупки пользователь {admin.get_details()}"  # информация об администраторе
        # return details
    
    
        details = f"{customer.get_details()} приобрел:\n"  # информация о покупателе
        for item in self.items:
             product_details = item["Продукт"].get_details()  # Получаем информацию о продукте
             item_quantity = item["количество"]  # Получаем количество продукта
             details += f"{product_details}, Количество: {item_quantity}\n"
        details += f"Общая стоимость: {self.get_total()} руб\n"
        details += f"Зарегистрировал покупки пользователь {admin.get_details()}"  # информация об администраторе
        return details