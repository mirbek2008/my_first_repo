
# people = ["Tom", "Sam", "Bob"]
# print(people)
#
# people[1] = "Mike"
# print(people)
# #
# people[2] = "Ayana"
# print(people)
#
#
# people = [1, 2, 3, 4]
#
# num3, num2, num1, num4 = people
#
# print(num3)
#
#
# people = ["Tom", "Sam", "Bob"]
#
# for i in people:
#     print(i)
#
# i = 0
# while i < len(people):
#     print(people[i])
#     i += 1

# #
# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
#
# slice_people1 = people[:4]
# print(slice_people1)
#
# slice_people2 = people[1:3]  # с 1 по 3
# print(slice_people2)  # ["Bob", "Alice"]
# #
# slice_people3 = people[1:6:3]  # с 1 по 6 с шагом 2
# print(slice_people3)  # ["Bob", "Tim"]
#
#
# people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
#
# slice_people1 = people[:-1]  # с предпоследнего по нулевой
# print(slice_people1)  # ["Tom", "Bob", "Alice", "Sam", "Tim"]
# #
# slice_people2 = people[0]  # с третьего с конца по предпоследний
# print(slice_people2)  #
#
#
# students = ["Ainazik", "Ayana"]
# # print(students)
# # students.append("Azamat")
# # print(students)
# # #
# students.insert(0, "Nursultan")
# print(students)
# print(students[2])














# def find_max_in_list(zamirbek):
#     maximum = zamirbek[0] # 99
#     for i in zamirbek:
#         if i > maximum:
#             maximum = i
#     return maximum
#
#
# lst = [10, 20, 400, 45, 99]
# print(find_max_in_list(lst))
#
#
# def remove_duplicates(my_list):
#     new_list = [] # 10, 20, 30, 50, 60, 40, 80
#     for i in my_list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
#
#
# mirbek = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# print(remove_duplicates(mirbek))
#
#
# def reverse_list(lst):
#     return lst[::-1]
#     new_list = []
#     for i in lst:
#         new_list.insert(0, i)
#     return new_list
#
#
# lst = [10, 20, 30, 40, 50]
# print(reverse_list(lst))
#
#
# def sum_of_list(lst):
#     sum = 0 # 150
#     for i in lst:
#         sum += i
#     return sum
#
#
# lst = [10, 20, 30, 40, 50]
# print(sum_of_list(lst))
#

# def is_palindrome(lst):
#     if lst == lst[::-1]:
#         return True
#     else:
#         return False
#
#
# lst = [10, 20, 10]
# print(is_palindrome(lst))


# def multiple_list(lst):
#     result = 1
#     for i in lst:
#         result *= i
#     return result
#
#
# lst = [2, 2, 4, 3, 2]
# print(multiple_list(lst))
#
#
# def odd(lst):
#     new_list = [] # 21, 45, 93
#     new_list2 = []
#     for i in lst:
#         if i % 2 != 0:
#             new_list.append(i)
#     return new_list
#
#
# lst = [10, 21, 4, 45, 66, 93]
# print(odd(lst))














# def find_max_in_list():
#     number = [3, 5, 7]
#     number2 = max(number)
#     print(number2)
#
# find_max_in_list()



# def remove_dublicates():
#     num = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5,]
#     print(f"Старый список: {num}\n")
#     print(f"новый список: {list(dict.fromkeys(num))}")
#
# remove_dublicates()



# def reverse_list():
#     num = [1, 2, 3, 4, 5]
#     num.reverse()
#     print(num)
#
# reverse_list()



# def sum_of_list():
#     num = [1, 2, 3, 4, 5,]
#     num2 = sum(num)
#     print(num2)
#
# sum_of_list()


# def word_palindromes():
#     word = ["asa"]
#     word2_palindromes = [number if str(number) == str(number)[::-1] else 'no' for number in word ]
#     print(*word2_palindromes)
#
# word_palindromes()




# def multiplication():
#     num = [1, 2, 3, 4, 5]
#     for num2 in num:
#         f = 1
#         for i in range(1, num2 + 1):
#             f *= i
#     print(f)
#
# multiplication()




# def find_odd_numbers():
#     num = [34, 33, 55, 65, 30,]
#     print(f"все числы: {num}")
#     for a in num:
#         if a % 2 != 0:
#             print(f"нечетные числы: {a} ")
#
# find_odd_numbers()






# def capitalize_if_starts_with(strings, letter):
#     if strings[0] == letter:
#         print(strings.capitalize())
#     else:
#         print(strings)
#
# capitalize_if_starts_with("hello", "h")




