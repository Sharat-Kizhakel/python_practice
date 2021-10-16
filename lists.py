# lists
# animals = ["cat", "dog", "moose", "tiger"]
# breed = ["type1", "type2", "type3"]
# expense = ["less", "more", "lot"]
# mix_breed = [animals, breed, expense]
# print(mix_breed[1][2])
# print(animals[0])

# for x in animals:
#     print(x)

# animals.insert(1, "lol")
# animals.sort()
# print(animals)

# tuples immutable
student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))

# set
# UNORDERED collection no duplicate values

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "knife", "bowl", "silver spoon"}
# utensils.add("napkin")
# utensils.remove("fork")
# dinner_table = utensils.union(dishes)
# utensils.clear()
# utensils.update(dishes)
# for x in dinner_table:
# print(x)

# A-B difference
print(utensils.difference(dishes))
# what does utensils have that dishes doesn't
print(utensils.intersection(dishes))
