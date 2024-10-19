# def  my_decorator(func):
#     def wrapper():
#         print("hello")
#         resultat = func()
#         print("bye")
#         return resultat
#     return wrapper
#
#
# def my_func():
#     print("My function")
#
#
#
# m = my_decorator(my_func)
# m()
import time


# def my_name(name):
#     def a():
#         print("start osnovnoi funcsii")
#         resul = name()
#         print("kones osnovnoi funcsii")
#         return resul
#     return a
#
# def my_func():
#     print("my name is mirbek")
#
# m = my_name(my_func)
# m()



# def osnovnoi_func(igra):
#     def add():
#         start_igra()
#         igra()
#         level()
#         stop_igra()
#     return add
#
# @osnovnoi_func
# def ball():
#     print("vash ball")
# def start_igra():
#     print("start igra")
# def stop_igra():
#     print("stop igra")
# def level():
#     print("level")
#
# ball()




# def osnovnoi_func(func):
#     def wrapper():
#         start()
#         func()
#         stop()
#     return wrapper
# def start():
#     print("start cecii ")
# def stop():
#     print("stop cesii")
# @osnovnoi_func
# def dobavit():
#     print("dobavit")
# @osnovnoi_func
# def pokupca():
#     print("pokupka")
# dobavit()
# pokupca()
















# def matimatika(func):
#     def calculator(*args):
#         start()
#         res = func(*args)
#         stop()
#         return res
#     return calculator
#
# @matimatika
# def add(a, b):
#     print(f"{a} + {b} = {a + b}")
#
# @matimatika
# def subtract(a, b):
#     print(f"{a} - {b} = {a - b}")
#
# @matimatika
# def multiply(a, b):
#     print(f"{a} * {b} = {a * b}")
#
# @matimatika
# def divide(a, b):
#     if a / b:
#         print(f"{a} / {b} = {a / b}")
#     elif a / 0 or b / 0:
#         print("нельзя делит на ноль !!!!")
#
# def start():
#     print("старт работы колькулятора")
# def stop():
#     print("завершение работы колькулятора")
#
#
# add(4, 8)
# subtract(10, 5)
# multiply(2, 4)
# divide(20, 2)
#
#
#
#
#
# def create_order(func):
#     def order_notification():
#         start()
#         func()
#         stop()
#     return order_notification
# @create_order
# def order():
#     print("menu")
#     print("1 juice")
#     print("2 coffee")
#     print("3 tea")
#
#     order = int(input("your order: "))
#     name = input("your name: ")
#     if order == 1:
#         print(f"juice for {name}")
#     elif order == 2:
#         print(f"coffee for {name}")
#     elif order == 3:
#         print(f"tea for {name}")
#     else:
#         print("it's not on the menu")
#
#
# def start():
#     print("start order")
#
#
# def stop():
#     print("stop order")
#
#
# order()





# def repeat(times):
#     def decorator(func):
#         def wrapper(*args):
#             for i in range(times):
#                 print(f"Вызов {i+1}:")
#                 result = func(*args)
#                 print(result)
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def greet(name):
#     return f"Привет, {name}!"
#
# greet("mirbek")








# import random
#
# def attack(func):
#     def log_turn():
#         start()
#         func()
#         stop()
#     return log_turn
#
#
# def name_character():
#     print("вы")
#
#
# def name_enemy():
#     print("враг")
# #
# #
# @attack
# def damage():
#     print(f"игра 'победи врага'")
#     name_character()
#     name_enemy()
#     print("hp врага ***")
#     while True:
#         f = [300, 400, 500, 800, 900]
#         n = random.choice(f)
#         print(n)
#         d = int(input("сила атаки: "))
#         if d >= n:
#             print(f"атака {d} : {n} hp врага")
#             print("вы победили!!")
#         elif d < n:
#             print(f"ваш удар {d} : {n} hp врага")
#             print("вы проиграли")
#
#         t = input("желлайте играть еще yes or on: ")
#         if t == "yes":
#             continue
#         else:
#             print("спасибо за игру")
#             break
#
#
# def start():
#     print("начала игры")
#
#
# def stop():
#     print("конец игры")
#
#
# damage()































