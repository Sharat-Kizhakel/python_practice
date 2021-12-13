# filter() = creates a collection of elements from an iterable for
# which a function returns True
#Syntax: filter(function,iterable)
friends = [("sharat", 21), ("josh", 19), ("Freddy", 16),
           ("David", 20), ("winnetou", 18), ("lol", 17)]

of_age = lambda eligible: eligible[1] > 18
greater_than_18 = filter(of_age, friends)
for i in greater_than_18:
    print(i[0])
