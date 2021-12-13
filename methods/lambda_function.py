# lambda function= function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression.
# (like a shortcut)

# SYNTAX: lambda parameters:expression

# w/o lambda

# def double(x):
#     return x * 2


# print(double(3))

# with lambda
# returns a function object
# double=lambda x:x*2
# print(double(5))

multiply = lambda x, y, z: x * y * z
print(multiply(3, 2, 4))
check_age = lambda age: True if age >= 18 else False
print(check_age(10))
