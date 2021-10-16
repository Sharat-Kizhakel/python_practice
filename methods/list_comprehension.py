# list comprehension a way to create a new list with less syntax
#list=[expression for item in iterable]

# without list compre
# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

# with list compre
# squares = []
# squares = [(i * i) for i in range(1, 11)]
# print(squares)

# can be used to mimic lambda functions
# with lambda
# students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 65]
# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)

# with list comprehension
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 65]
distinction = [mark for mark in students if mark >= 60]
print(distinction)
# note if you need else condition then syntax is:
# list=[expression (if/else) for item in iterable]
# list=[expression for item in iterable if conditional]
