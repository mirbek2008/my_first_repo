# names = {"m": "mirbek", "a": "ainazik", "r": "aiana", "k": "zamirbek"}
# n = names["r"]
# print(n)
import list

# for i in names.items():
#     print(i)


# for i in names.values():
#     print(i)

# for i in names.keys():
#     print(i)


# fruits = {
#     "apple": 4,
#     "banan": 2,
#     "oreng": 7
# }
# n = fr"uits["apple"]
# if n > 3:
#     print(n + 3)
# else:
#     print(n - 1)




# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# for key, value in users.items():
#     print(f"Phone: {key}  User: {value} ")

# users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
# students = users.copy()










# s = "hello world"
# s2 = {i: s.count(i) for i in set(s)}
# print(s2)


# s = [1, 2, 3]
# sl = ["one", "two", "three"]
# s1 = dict(zip(s, sl))
# print(s1)


# s3 = dict.fromkeys([1, 2, 3], "numbers")
# print(s3)







# animals = {
#     "kot": "cat",
#     "mish": "mouse",
#     "cabaka": "dog"
#
# }
#
# n = input("saz: ")
# if n in animals:
#     print(f"clovo {n} perevod {animals[n]}")
# else:
#     print("nenaiden")









# def invent_dict(d):
#     n = {i: i_2 for i_2, i in d.items()}
#     return n
#
# dct = {"a": "b", "c": "d"}
# res = invent_dict(dct)
# print(res)




# def dict_to_tuple_list(func):
#     list_1 = list((func.items()))
#     return list_1
#
# n = {"Akdil": 10, "Fatima": 15, "Mirbek": 20}
# res = dict_to_tuple_list(n)
# print(res)




# grades = {
#     'Аяна': 96, 'Акдил': 89, 'Талгарбек': 75, 'Бибигул': 69,
#     'Мирбек': 89, 'Айназик': 81, 'Медербек': 80, 'Кудайберди': 86,
#     'Фатима': 84, 'Замирбек': 91, 'Азамат': 13
# }
# def students(func):
#     n = {i: i_2 for i, i_2 in func.items() if i_2 > 80}
#     n1 = {i: i_2 for i, i_2 in func.items() if i_2 < 80}
#     return n, n1
#
#
#
# n, n1 = students(grades)
# print(f"прошли {n}")
# print(f"не прошли {n1}")













# my_dict = {}
# my_dict["name"] = "jon"
# print(my_dict)





# fruots = {"apple": 5, "banan": 7, "oreng": 3}
# print(fruots["apple"])



# person = {"name": "Alica", "age": 30, "city": "osh"}
# print(person["age"])


# fruots = {"apple": 5, "banan": 7, "oreng": 3}
# print(fruots["banan"] + 2)


# fruots = {"apple": 5, "banan": 7, "oreng": 3}
# print("apple" in fruots)





# person = {"name": "Alica", "age": 30, "city": "osh"}
# print(person.keys())


# fruots = {"apple": 5, "banan": 7, "oreng": 3}
# print(fruots.values())


# person = {"name": "Alica", "age": 30, "city": "osh"}
# for i in person.items():
#     print(i)





# fruots = {"apple": 5, "banan": 7, "oreng": 3}
# del fruots["oreng"]
# print(fruots)





# my_dict = {"name": "lone"}
# print(my_dict.clear())











# grades = {
#     'Аяна': 96, 'Акдил': 89, 'Талгарбек': 75, 'Бибигул': 69,
#     'Мирбек': 89, 'Айназик': 81, 'Медербек': 80, 'Кудайберди': 86,
#     'Фатима': 84, 'Замирбек': 91, 'Азамат': 13
# }
# def students():
#     n = {}
#     n1 = {}
#     for keys, values in grades.items():
#         if values >= 80:
#             n[keys] = values
#         else:
#             n1[keys] = values
#     return f"Прошли {n}\nНе прошли {n1}"
# res = students()
# print(res)








# text = "My my name Aiana aiana"
# def func(text):
#     w = text.lower().split()
#     dct = {}
#     for i in w:
#         if i in dct:
#             dct[i] += 1
#         else:
#             dct[i] = 1
#     return dct
#
# res = func(text)
# print(res)



# num = [1, 2, 3, 4, 5]
# def numbers(num):
#     num2 = {}
#     for i in num:
#         num2[i] = i ** 2
#     return num2
#
# res = numbers(num)
# print(res)



# num = [1, 2, 3, 4, 5]
# def func(num):
#     n = {i: i ** 2 for i in num}
#     return n
#
#
# res = func(num)
# print(res)





# num1 = {1: 10, 2: 20, 3: 30}
# num2 = {1: 20, 5: 89, 8: 67}
# def func(num1, num2):
#     s = dict(num1)
#
#     for key, values in num2.items():
#         if
#
#






#жисон






#import random


# animals = {
#     'слон': 'Это самое большое наземное животное.',
#     'тигр': 'Это полосатый хищник.',
#     'панда': 'Это черно-белое животное, которое ест бамбук.',
#     'крокодил': 'Это рептилия, которая живет в воде.',
#     'коала': 'Это сумчатое животное, которое обитает в Австралии.',
# }
# #
# def guess_animal_game(my_dict):
#     print("Угадайте животное!")
#     list_1 = list(my_dict.items())
#     while True:
#         random_animals_1 = random.choice(list_1)
#         h = []
#         for i in random_animals_1:
#             if i not in h:
#                 h.append(i)
#         t = [h]
#         dct = dict(t)
#         for key, values in dct.items():
#             print(f"Подсказка: {values}")
#         n1 = input("Введите ваше предположение: ")
#         if n1 in dct.keys():
#             print("Вы угадали!!!")
#         else:
#             print("Не угадали")
#         answer = input("Желаете попробовать еще раз? да или нет: ")
#         if answer == "да":
#             continue
#         else:
#             for key, values in dct.items():
#                 print(f"Спасибо за игру. Загаданное животное было {key}")
#             break
#
#
#
# guess_animal_game(animals)







# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR',
#       		2:'DG',
#       		3:'BCMP',
#       		4:'FHVWY',
#       		5:'K',
#       		8:'JZ',
#       		10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ',
#       		2:'ДКЛМПУ',
#       		3:'БГЁЬЯ',
#       		4:'ЙЫ',
#       		5:'ЖЗХЦЧ',
#       		8:'ШЭЮ',
#       		10:'ФЩЪ'}
# text = input("напиши слова: ").upper()
# if isCyrillic(text):
# 	print(f"очко: {sum([k for i in text for k, v in points_ru.items() if i in v])}")
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))



print("python")









































