# sort() method=used with ONLY WITH list!!
# sorted() function=used with iterables(OTHER THAN LIST !!!!)

# 1.
# students = ["joe", "shere", "derry", "Ann"]
# students.sort(reverse=True)

# for i in students:
#     print(i)


# 2. with other iterables
# students = ("joe", "shere", "derry", "Ann")
# # note how syntax is different
# sorted_students = sorted(students)
# for i in sorted_students:
#     print(i)


# # complex examples
# students = [("joe", "F", 30), ("shere", "A", 40),
#             ("derry", "B", 20), ("Ann", "C", 100)]
# students.sort()
# for i in students:
#     print(i)
# print("\n")
# sorting by grade
# note grade contains a function which will be executed on every list element
# grade = lambda grades: grades[1]
# print(grade)
# students.sort(key=grade)
# for i in students:
#     print(i)
# print("\n")
# age = lambda ages: ages[2]
# # sorting by reverse order of age
# students.sort(key=age, reverse=True)
# for i in students:
#     print(i)

# sorting a tuple
age = lambda element: element[2]
students = (("joe", "F", 30), ("shere", "A", 40),
            ("derry", "B", 20), ("Ann", "C", 100))
# key takes a function
sorted_students = sorted(students, key=age)
for i in sorted_students:
    print(i)
