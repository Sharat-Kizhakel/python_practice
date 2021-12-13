# passing object as argument

class Car:
    color = None


def change_color(car, color):
    car.color = color


car1 = Car()
car2 = Car()
change_color(car1, "blue")
change_color(car2, "green")
print(car1.color)
print(car2.color)
