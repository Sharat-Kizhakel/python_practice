# walrus operator :=
# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# without walrus operator

# foods = list()

# while True:
#     food = input("What food do you like?:")
#     if food == "quit":
#         break
#     foods.append(food)

# with walrus operator

foods = list()
# it automatically returns the food we enter into food var adn so we can check for quit in the same line
# otherwise traditional assignment stores it in food var
#  then we need to use '==' to check for equality with quit
# thus making the code longer
while food := input("What food do you like?:") != "quit":
    foods.append(food)
