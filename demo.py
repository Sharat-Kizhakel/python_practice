# import math
# name = "Bro"
# print(name)
# print(len(name))
# print(name.find('o'))
# print(name.capitalize())
# print(name.isdigit())
# print(name.isalpha())
# print(name.replace("o", "a"))
# print(name*3)

# x = 1
# y = 2.0
# z = "3"
# print(int(y))
# print(z*3)

# user input in python

# name = input("What is your name:")
# age = int(input("What is your age"))
# height = float(input("How tall are you:"))
# print("Hello :"+name)
# print("Age:{}".format(age))

# math function
# import math
# pi = -3.14
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(420))

# string slicing

name = "ha this funny"
f_name = name[0:4]
# or
f_name1 = name[:4]
step_demo = name[0:len(name):2]
# reverse using slicing
rev_name = name[::-1]
print(f_name)
print(f_name1)
print(step_demo)
print(rev_name)

# slice function
website = "http://google.com"
slice = slice(7, -4)
print(website[slice])
