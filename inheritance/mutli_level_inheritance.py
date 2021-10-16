# MULTILEVEL INHERITANCE:when a derived class inherits another derived(child ) class
# its like a hierarchy
class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("this animal is eating")


class Dog(Animal):
    def bark(self):
        print("The dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
