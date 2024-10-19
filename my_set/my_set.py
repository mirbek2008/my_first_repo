# #set == множества
#
#
#
# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
#
# people = ["Mike", "Bill", "Ted", "Bill"]
# print(people)
#
# users = set(people)
# print(users)
#
# users = set()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# print(len(users))
#
# users = set()
# users.add("Sam")
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# user = "Tom"
#
# if user in users:
#     users.remove(user)
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# users.discard("Tim")
# print(users)
#
# users.discard("Tom")  # элемент "Tom" есть, и метод удаляет элемент
# print(users)  # {"Bob", "Alice"}
#
# users.clear()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# users = {"Tom", "Bob", "Alice"}
#
# students = users.copy()
# print(students)
#
# users = {"Tom", "Bob", "Alice"}
#
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# print(users | users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.intersection(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# print(users & users2)
#
# users = {"Tom", "Bob", "Alice", "Sam"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users2.intersection_update(users)
# print(users2)
# #
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.difference(users2)
# print(users3)
# print(users - users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.symmetric_difference(users2)
# print(users3)
#
# users4 = users ^ users2
# print(users4)
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers)) # True
#
# print(superusers.issubset(users)) # False
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers)) # False
# print(superusers.issuperset(users)) # True
#
# #-----------------frozen set---------------
# users = {"Tom", "Bob", "Alice"}
#
# users = frozenset({"Tom", "Bob", "Alice"})












# name = {"tom", "tim", "alica"}
#
# n = "tim"
#
# if n in name:
#     name.remove(n)
#
# print(name)

# name.discard("toma")
# print(name)
#
# users = {"tom", "tim", "tom"}
# users2 = {"alica", "tom", 'tim'}
# n = users.union(users2)
# print(n)
# print(users | users2)



# users = {"Tom", "Bob", "Alice",}
# users2 = {"Sam", "Kate", "Bob", "Tom"}

# users3 = users.intersection(users2)
# print(users3)
# print(users & users2)














# sentence = "apple", "banan", "orange", "apple", "lemon", "banan"
# print(set(sentence))



# list_1 = [1, 2, 3, 4, 5]
# list_2 = [4, 5, 6, 7, 8]
# set_1 = set(list_1)
# set_2 =set(list_2)
# print(set_1.intersection(set_2))




# list_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6  ]
# set_1 =set(list_1)
# print(list(set_1))



# str_1 = "hello wolrd"
# print(set(str_1))




# frozen_set = frozenset({1, 2, 3, 4, 5})
# frozen_set.discard(6)
# print(frozen_set)#тип frozen set неизменяемый



# frozenset_1 = frozenset({1, 2, 3, 4, 5})
# frozenset_2 = frozenset({4, 5, 6, 7, 8})
# print(frozenset_1.intersection(frozenset_2))



# frozenset_1 = frozenset({"Tim", "Tom", "Bob"})
# frozenset_1.discard("Tom")
# print(frozenset_1)#тип frozen set неизменяемый



# list_1 = [1, 2, 3, 3, 4, 4, 5]
# print(frozenset(list_1))
















