# str.firmat()

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the lazy {0}".format(animal, item))
print("The {god} jumped over the {food} nd another {god}".format(
    god="cow", food="moon"))
# adds spaces
print("Hello my name is {:10}".format(animal))
print("Hello my name is {:^10}".format(animal))
print("Hello my name is {:<10}".format(animal))
print("Hello my name is {:>10}".format(animal))

number = 3.14159
num1 = 1000
print("The no is {:.2f}".format(number))
print("the no in binary is {:b}".format(num1))
print("the no in binary is {:o}".format(num1))
print("the no in binary is {:x}".format(num1))
print("the no in binary is {:E}".format(num1))
