# **kwargs= parameter that will pack all arguments into a dictionary
# *args packs it into a tuple
# and to sequentially access it you need to use to convert the tuple back into a list

def welcome(**kwargs):  # note the name can be anything not necessarily kwargs imp thing is it should be preceded by **
    print("Hello "+kwargs['first']+" "+kwargs['last'])
    for key, value in kwargs.items():
        print(key, value, end=", ")


welcome(first="Sharat", middle="Prasad", last="Kizhakel")
