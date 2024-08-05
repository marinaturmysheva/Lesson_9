from classes.products import Electronics, Clothing, WashingPowder, CleaningGel
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
washing_powder = WashingPowder (name="Стиральный порошок Персил", price=1699, weight="14000")
cleaning_agent = CleaningGel (name= "Чистящее средство для ванной Cif", price=175, volume = "500")



# Создаем пользователей
customer = Customer(username = "Mikhail", email = "python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="root", email = "root@derkunov.ru", admin_level = 5)


# Создаем корзину покупок и добавляем товары
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(washing_powder, 2)
cart.add_item(cleaning_agent, 5)


# Выводим детали корзины
#print(cart.get_details())


# Выводим детали корзины, передавая объекты Customer и Admin в качестве аргументов
print(cart.get_details(customer, admin))
