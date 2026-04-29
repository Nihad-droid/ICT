# """Methods for lists:
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list alphabetically (numbers first)
#
#
# *Difference between "remove and pop" is, remove requires you to put the value while pop needs you
# to write its position.
# """
#
# my_list1 = ["Sodium", "Fluorine", "Uranium", "Polonium", "Potassium", "Kryptonite", "Helium"]
# my_list2 = ["Gravity", "Thermodynamics", "Quantum Mechanics", "Electric", "Optics", "Relativity"]
#
# print(my_list2.append("Alkanes"))
# print(my_list2.copy())
# print(my_list2.count("Thermodynamics"))
# print(my_list2.extend(my_list1))
# print(my_list2.index("Electric"))
# print(my_list2.insert(1, "Kinetics"))
# print(my_list2.pop(3))
# print(my_list2.remove("Alkanes"))
# print(my_list2.reverse())
# print(my_list2.sort())
# print(my_list2.clear())


# def divisor(x):
#     def dividend(y):
#         def divis2(z):
#             def divis3(t):
#                 return x+y+z+t
#             return divis3
#         return divis2
#     return dividend
#
#
# divide = divisor(2)
# divis = divide(100)
# print(divisor(10)(100)(10000)(1000))


# def double(x):
#     return x * 2
#
#
# print(double(5))


# double = lambda x:x * 2
# multiply = lambda x, y:x * y
# addition = lambda x, y, z: x + y+ z
# fullname = lambda firstname, lastname: firstname + lastname
# agecheck = lambda age:True if age >= 18 else False
# print(double(6))
# print(multiply(5,6))
# print(addition(3,4,5))
# print(agecheck(15))
# print(fullname("niko", " memmedli"))


# students = ['squidward', 'sandy', 'patrick', 'spongebob', 'mr.krabs']
#
# students.sort()
#
# for i in students:
#     print(i)


# students = (('squirward', 'f', 60),
#             ('sandy', 'a', 33),
#             ('patrick', 'd', 36),
#             ('spongebob', 'b', 20),
#             ('mr krabs', 'c', 78))
# grade = lambda grades:grades[2]
# # students.sort(key=grade)  "use this if tuples inside list
# sorted_students = sorted(students, key=grade)       # "use this if tuples inside tuple"
# for i in sorted_students:
#     print(i)


# store = [('shirt', 20.00),
#          ('pants', 25.00),
#          ('jacket', 50.00),
#          ('socks', 10.00)]
#
# to_euros = lambda data: (data[0],data[1]*0.82)
#
# store_euros = list(map(to_euros, store))
#
# for i in store_euros:
#     print(i)


# friends = [("Rachel", 19),
#            ("Monica", 18),
#            ("Phoebe", 17),
#            ("Joey", 16),
#            ("Chandler", 21),
#            ("Ross", 20)]
#
# age = lambda data:data[1] >= 18
# drinkingbuddies = (list(filter(age, friends)))
# for i in drinkingbuddies:
#     print(i)


# import functools
# letters = ['H', 'E', 'L', 'L', 'O']
# word = functools.reduce(lambda x, y: x + y, letters)
# print(word)
# factorial = [1,2,3,4,5]
# result = functools.reduce(lambda x, y: x * y, factorial)
# print(result)


# squares = []
# for i in range(1,11):
#     squares.append(i * i)
# print(squares)
#
# squares = [i * i for i in range(1,11)]
# print(squares)

# students = [100,90,80,70,60,50,40,30,0]
# passed_students = list(filter(lambda x: x >= 60, students))
# passed_students = [i for i in students if i >= 60]
# passed_s
# print(passed_students) #both works the same

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

weather = {'New York': 'snowing', 'Boston': 'Sunny', 'Los Angeles': "Sunny", 'Chicago': 'Cloud'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'Sunny'}
print(sunny_weather)