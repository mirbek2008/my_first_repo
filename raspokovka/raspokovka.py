



# x, y, z = 1, 2, 3
# print(x)
# print(y)
# print(z)

# x, y = (1, 2)
# print(x)
# print(y)

# name, age, company = ("Tom", 38, "Google")
# print(name)
# print(age)
# print(company)

# people = ["Tom", "Bob", "Sam"]
# first, second, third = people
# print(first)      # Tom
# print(second)     # Bob
# print(third)

# dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
# r, b, g = dictionary
# print(r)    # red
# print(b)    # blue
# print(g)    # green
# # получаем значение по ключу
# print(dictionary[g])

# people = [
#     ("Tom", 38, "Google"),
#     ("Bob", 42, "Microsoft"),
#     ("Sam", 29, "JetBrains")
# ]
#
# for name, age, company in people:
#     print(f"Name: {name}, Age: {age}, Company: {company}")

# people = ["Tom", "Bob", "Sam"]
#
# for index, name in enumerate(people):
#     print(f"{index}.{name}")

# person =("Tom", 38, "Google")
# name, _, company = person
# print(_)
# print(name)     # Tom
# print(company)  # Google

# num1=1
# num2=2
# num3=3
#
# *numbers,=num1,num2,num3
# print(numbers)

# head, body, *tail = [1, 2, 3, 4, 5]
#
# print(head)  # 1
# print(body)  # 2
# print(tail)  # [3, 4, 5]

# *head, tail = [1, 2, 3, 4, 5]
#
# print(head)
# print(tail)

# head, *middle, tail = [1, 2, 3, 4, 5]
#
# print(head)
# print(middle)
# print(tail)

# first, second, thrid, *other = [1, 2, 3, 4, 5]
#
# print(first)  # 1
# print(second)  # 2
# print(thrid)  # 3
# print(other)

# first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print(first)  # 1
# print(third)  # 3
# print(last)

# red, *other, green = {"red": "красный", "blue": "синий", "yellow": "желтый", "green": "зеленый"}
#
# print(red)  # red
# print(green)  # green
# print(other)

# nums1 = [1, 2, 3]
# nums2 = (4, 5, 6)
#
# # распаковываем список nums1 и кортеж nums2
# nums3 = [*nums1, *nums2]
# print(nums3)  # [1, 2, 3, 4, 5, 6]

# dictionary1 = {"red": "красный", "blue": "синий"}
# dictionary2 = {"green": "зеленый", "yellow": "желтый"}
#
# # распаковываем словари
# dictionary3 = {dictionary1, dictionary2}
# print(dictionary3)

# def fun(*args):
#     # обращаемся к первому элементу кортежа
#     print(args[0])
#
#     # выводим весь кортеж
#     print(args)
#
#
# fun("Python", "C++", "Java", "C#")

# numbers = [1, 2, 3]
#
# def sum(*args):
#     result = "0"
#     for arg in args:
#         result += arg
#     return result


# print(sum("1", "2"))

# list1 = [1, 2]
# list2 = [3, 4, 5]
#
# if len(list1) == len(list2):
#     combined_list = [*list1, *list2]
#     print("Объединенные списки:", combined_list)
# else:
#     print("Списки не имеют одинаковой длины.")




# names = ["tom", "bob", "tim", "jeck"]
# tom, bob, tim, jeck = names
# print(tom)
# print(bob)
# print(tim)
# print(jeck)
#
# tom, _, tim, _, = names
# print(tom)
#
# print(tim)

# my_name = "mirbek"
# m, i, r, b, e, k = my_name
# print(m)
# print(i)
# print(r)
# print(b)
# print(e)
# print(k)



# my_name = "mirbek"
# _, *i, _ = my_name
# print(i)


# my_name = "mirbek"
# *_, k = my_name
# print(k)


# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# if len(num1) == len(num2):
#     n = [*num1, *num2]
#     print(n)
# else:
#     print("num1 != num2")



















# d, a = (20, 10)
# print(d)
# print(a)


# max_list = [1, "hello", (10, 20), [30, 40]]
# int_1, str_1, tuple_1, list_1 = max_list
# print(int_1)
# print(str_1)
# print(tuple_1)
# print(list_1)



# def print_coordinates(ar_1, ar_2, ar_3):
#     coordinates = [ar_1, ar_2, ar_3]
#     num1, num2, num3 = coordinates
#     print(num1)
#     print(num2)
#     print(num3)
#
# print_coordinates(10, 20, 30)




# data = [[10, 20], [30, 40], [50, 60]]
# y = 0
# while y < 1:
#     y += 1
#     list_1, list_2, list_3 = data
#     print(list_1)
#     print(list_2)
#     print(list_3)
#
#     n = list_1, list_2, list_3
#     (h, t), (j, l), (o, p) = n
#     print(h)
#     print(t)
#     print(j)
#     print(l)
#     print(o)
#     print(p)


# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num_1, num_2, num_3, *num_4, num_5, num_6 = data
# print(num_1)
# print(num_2)
# print(num_3)
# print(num_4)
# print(num_5)
# print(num_6)


# data = [7, 14, 21, 28]
# num1, num2, num3, num4 = data
# n = num1 // 7, num2 // 7, num3 // 7, num4 // 7
# a, b, c, d = n
# print(a, b, c, d)


# list_1 = [100, 200]
# list_2 = [300, 400, 500, 600]
# num_1, *num_2 = list_1
# num_3, *num_4 = list_2
# b = [num_1,  num_3]
# n = num_2 + num_4
# print(b)
# print(n)






