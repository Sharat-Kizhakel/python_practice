# method overriding is a way for a child class to provide its own implementation of a method already defined in parent class

class Animal:
    def eat(self):
        print("The animal is eating")


class Rabbit(Animal):
    def eat(self):  # overriding
        print("the rabbit is eating a carrot")


        # When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.
rabbit = Rabbit()  # base class implementation given pref
animal = Animal()  # animal class impl. given preference
rabbit.eat()
animal.eat()
