# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(my_list[10])
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except BaseException:
#     print("Общее исключение")
# finally:
#     print("Блок try завершил выполнение")



#
# try:
#     number = int(input("1chi san: "))
#     number2 = int(input("2chi san:"))
#     number3 = number / number2
# except ValueError as e:
#     print("san jaz", e)
# except ZeroDivisionError as e:
#     print("nolgo bolunboit", e)
# except Exception as e:
#     print("try ishtegen jok", e)
# finally:
#     print("zavershenie raboti")



# numbers = input("Введите список чисел, разделенных пробелами: ").split()
# n = 0
# for i in numbers:
#     try:
#         n += int(i)
#     except ValueError:
#         print("ushul tamgani karmadik", i)
#     except Exception:
#         print('ishtegen jok')
#     finally:
#         print(" zavershenie raboti")
# print(n)



# try:
#     num = int(input())
#     num2 = int(input())
#     try:
#         num3 = num / num2
#         print(num3)
#     except ZeroDivisionError as e:
#         print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("zavershenie raboti")




















#shop = {
#     "меч": 100,
#     "щит": 150,
#     "зелье": 50,
# }
# balance = 300
# def buy_item(item, quantity, balance):
#     try:
#        if item in shop.keys():
#             g = []
#             for i in range(quantity):
#                 g.append(shop[item])
#             print(f"Ваш баланс {balance}")
#             print(f"{item}: всего {sum(g)}$")
#             if balance >= sum(g):
#                 print(f"У вас осталось: {balance - sum(g)}$")
#             else:
#                 print("нехватает баланса")
#        else:
#            print("У нас нет такого товара")
#
#
#     except ValueError as e:
#         print("надо писать количество", e)
#     except Exception as e:
#         print(e)
#
# buy_item("меч", 3, balance)
# buy_item("щит", 4, balance)
# buy_item("зелье", 5, balance)








#
#
# def get_student_data():
#     print("Регистрация студента")
#     while True:
#         try:
#             name = input("name: ").lower()
#             if name.isalpha():
#
#                 try:
#                     age = int(input("age: "))
#                     if age >= 0 and age < 100:
#                         try:
#                             number = int(input("number:+996 "))
#                             if number > 99999999 and number < 999999999:
#                                 print(f"name: {name}, age: {age}, number: {number}")
#                                 print("конец регистрации")
#                                 break
#                             else:
#                                 print("Несуществующий номер")
#                                 continue
#                         except ValueError as e:
#                                 print(e)
#                                 continue
#                     else:
#                         print("Некоректный возраст")
#                 except ValueError as e:
#                     print(e)
#                 continue
#             else:
#                 print("Некоректный имя")
#         except Exception as e:
#             print(e)
#
#
#
# get_student_data()






















# shop = {
#     "меч": 100,
#     "щит": 150,
#     "зелье": 50,
# }
# balance = 300
# def buy_item(item, quantity, balance):
#     try:
#        if item in shop.keys():
#             g = []
#             for i in range(quantity):
#                 g.append(shop[item])
#             print(f"Ваш баланс {balance}")
#             print(f"{item}: всего {sum(g)}$")
#             if balance >= sum(g):
#                 print(f"У вас осталось: {balance - sum(g)}$")
#             else:
#                 print("нехватает баланса")
#        else:
#            print("У нас нет такого товара")
#
#
#     except ValueError as e:
#         print("надо писать количество", e)
#     except Exception as e:
#         print(e)
#
# buy_item("меч", 3, balance)
# buy_item("щит", 4, balance)
# buy_item("зелье", 5, balance)




























































































































































