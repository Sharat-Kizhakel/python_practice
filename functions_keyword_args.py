# functions

def hello(name):
    print("hello"+name)


hello("sharat")


def whats_name(my_name, age):
    print("hello"+my_name+"and"+str(age))


my_name = "joe"
whats_name(my_name, 21)

# return value of a function


def multiply(no1, no2):
    result = no1*no2
    return result


x = multiply(2, 4)
print(x)

# keyword arguments
# these are argumnents preceded by an identifier when we pass them to a function.
# The order of the arguments doesn't matter, unlike positional arguments py knows the names of the arguments it receives

#this is positonal


def hello(name, last):
    print("hello "+name+""+last)


hello("john", "doe")
#this is keyword


def hello1(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)


hello1(middle="Prasad", last="Kizhakel", first="Sharat")
