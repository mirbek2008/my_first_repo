# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple))
#
# tom = "Tom", 23, 5, "tyt"
# print(tom)
#
# tom = ("tom", )
# print(type(tom))
#
data = ["Tom", 37, "Google"]

# tom = tuple(data)
# print(tom)
#
# tom = ("Tom", 37, "Google")
# print(len(tom))
#
# tom = ("Tom", 37, "Google", "software developer")
#
# print(tom[0])       # Tom
# print(tom[1])       # 37
# print(tom[-1])
#
# tom[1] = "Tim"
# print(tom[1])
#
# name, age, company, position = ("Tom", 37, "Google", "software developer")
# print(name)         # Tom
# print(age)          # 37
# print(position)     # software developer
# print(company)
#
# tom = ("Tom", 37, "Google", "software developer")

# print(tom[1:3])
#
# print(tom[:3])
#
# print(tom[1:])
#
# def get_user():
#     name = "Tom"
#     age = 22
#     company = "Google"
#     return name, age, company
#
#
# user = get_user()
# print(user)
#
# def print_person(name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# tom = ("Tom", 22)
# print_person(*tom, "Microsoft")
#
# bob = ("Bob", 41, "Apple")
# print_person(*bob)
#
# tom = ("Tom", 22, "Google")
#
# for i in tom:
#     print(i)
#
# tom = ("Tom", 22, "Google")
#
# i = 0
#
# while i < len(tom):
#     print(tom[i])
#     i += 1
#
# user = ("Tom", 22, "Google")
#
# name = "mom"
#
# if name in user:
#     print("Пользователя зовут Tom")
# else:
#     print("Пользователь имеет другое имя")
#
# my_tuple = (1, 2, 3, 1, 2, 1)

#
# count_of_1 = my_tuple.count(2)
# print(f"Число встречается {count_of_1} раз(а) в кортеже.")


# index_of_2 = my_tuple.index(2)
# print(f"Первое вхождение числа 2 находится по индексу {index_of_2}.")
#
# numbers = (3, 5, 7, 3, 9, 3, 5, 2, 8, 5)
#
# max_value = numbers[0] # 9
# min_value = numbers[0] # 2
#
# for number in numbers:
#     if number > max_value:
#         max_value = number
#     if number < min_value:
#         min_value = number
#
# print(f"Максимум: {max_value}")
# print(f"Минимум: {min_value}")














# number = (3, 4, 2, 6, 9, 2, 4, 5)
# max_1 = number[0]
# min_1 = number[0]
# for i in number:
#     if i > max_1:
#         max_1 = i
#     if i < min_1:
#         min_1 = i
# print(max_1)
# print(min_1)



# tuple_1 = ("mederbek", "mirbek", "aibek", "ian", "tom", "zamir")
# tuple_2 = tuple(i for i in tuple_1 if len(i) >= 5)
# print(tuple_2)
#
# tuple_2 = tuple(i for i in tuple_1 if i.startswith("a"))
# print(tuple_2)








# numbers = (4, 7, 8, 2, 5, 4, 6)
# numbers_2 = numbers.index(8)
# print(f"Первое вхождение числа 8 находится по индексу {numbers_2}")


# letters = ("a", "b", "c", "a", "d", "e", "a")
# letters_2 = letters.count("a")
# print(f"Буква 'a' встречается {letters_2} раз(а) в кортеже.")




# tuple_1 = (1, 2, 3, 4)
# tuple_2 = (5, 6, 7, 8)
# association = (*tuple_1, *tuple_2)
# print(association)


# tuple_1 = (1, 2, 3)
# tuple_2 = (1, 2, 3)
# if tuple_1 == tuple_2:
#     print("tuple_1 == tuple_2")
# elif tuple_1 != tuple_2:
#     print("tuple_1 != tuple_2")



# string = "hello"
# print(tuple(string))

# #
# tuple_1 = (1, 3, 5)
# tuple_2 = (2, 4, 6)
# resul = []
# for i in range(len(tuple_1)):
#     resul.append(tuple_1[i])
#     resul.append((tuple_2[i]))
# print(tuple(resul))




# def tuple1(tuple_1, tuple_2):
#     n = len(tuple_1)
#     n_2 = len(tuple_2)
#     if n != n_2:
#         print("n != n_2")
#
#     elif n == n_2:
#         list_1 = []
#         for i in range(len(tuple_1)):
#             list_1.append(tuple_1[i] + tuple_2[i])
#         return tuple(list_1)
#
# tuple_1 = (1, 2, 3)
# tuple_2 = (1, 2, 3)
# res = tuple1(tuple_1, tuple_2)
# print(res)
































