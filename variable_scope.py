
# using same var name for global and local scope
# python follows
# preferenc in decr order
# L=Local
# E=Enclosing
# G=Global
# B=Built-in

#global scope
name = "Bro"


def display_name():
    # local scope
    name = "Code"
    print(name)


display_name()
print(name)


# *args takes all args in function as tuple which needs to be iterated
def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0  # tuple doesnt support assignment
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))
