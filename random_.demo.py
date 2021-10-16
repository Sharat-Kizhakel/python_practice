# random function
import random

x = random.randint(1, 6)
y = random.random()

mylist = ["rock ", "paper", "scissors"]
z = random.choice(mylist)  # chooses random el from given sequence
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A"]
random.shuffle(cards)
print(cards)
print(y)
print(z)
print(x)
