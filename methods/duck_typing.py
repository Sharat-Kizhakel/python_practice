# DUCK TYPING: In this concept the class of an object is LESS important than the methods/attributes
# class type is NOT checked if min methods/attribures are present
# "If it walks like a duck, quacks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is quacking")


class Chicken:
    def walk(self):
        print("this chicken is walking")
    # if one these methods is missing then we cant pass it to person object

    def talk(self):
        print("this chicken is clucking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the duck")


duck = Duck()
chicken = Chicken()
person = Person()
person.catch(duck)
# even though the method is intended for duck,
# because the methods are the same as Chicken
# we are able to pass it to same method catch
person.catch(chicken)
# so class type is not checked
