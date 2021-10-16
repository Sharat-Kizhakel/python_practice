# method chaining= calling multiple methods sequentially. each call performs
# an action on the same object and returns self.

class Car:
    def turn_on(self):
        print("You start the car")
        return self

    def drive(self):
        print("You drive the car")
        return self  # to make use of method chaining return self

    def brake(self):
        print("You brake the car")
        return self

    def turn_off(self):
        print("You turn off the car")
        return self


def gap():
    print(20*"*")


car = Car()
car.turn_on()  # without method chaining i.e need to call sep
car.drive()  # without method chaining

car.turn_on().drive()  # with method chaining
# with method chaining
gap()
car.brake().turn_off()
gap()
# line continuation char '\' for readability
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
