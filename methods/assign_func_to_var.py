# in py even functions are objects

def hello():
    print("hello world")


hi = hello
hi()  # will get same output as hello() since mem locn of both will be same
hello()

say = print
say("i am same as print")
