class Animal:
    alive = True

    def eat(self):
        print("This is animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):  # inheritance is via the brackets
    def run(self):
        print("This rabbit is running")


class Fish(Animal):
    def swim(self):  # child classes can also have their own methods
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("The hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.run()
fish.eat()
fish.swim()
hawk.sleep()
hawk.fly()
