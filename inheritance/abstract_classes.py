# abstract classes:
# PREVENTS a user from creating an object of that class
# compels a user to override abstract methods in a child class
# abstract class= a class which contains one or more abstract methods
# abstract method=a method that has a declaration but doesnt have an implementation
# abc: abstract base class
from abc import ABC, abstractmethod  # needed to use abstr class


class Vehicle(ABC):  # by making vehicle class abstract we cant create an object of that type
    @abstractmethod  # decorator to make method abstract
    def go(self):
        pass  # method defined but no implementation
# note at least one abstract method has to be there in abstract class to prevent the abiltiy of instantiating class
# if go methdd wasnt there we still could have created a vehicle object

    @abstractmethod
    def stop(self):
        pass


class Bike(Vehicle):
    def go(self):
        print("riding a bike")

    def stop(self):
        print("STOP BIKE")


class Car(Vehicle):
    # if method go not overriden py will give error
    def go(self):
        print("riding a Car")

    def stop(self):
        print("stop a car")


# vehicle = Vehicle() trying to exec this will give error cuz we cant instantiate an abstract class it has no use anyways
car = Car()
bike = Bike()
car.go()
bike.stop()
# vehicle.go()  # no use cuz it just gives the blueprint
