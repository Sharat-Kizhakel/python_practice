# Higher order Function= a function either:
# 1.accepts a function as an arguments
# or
# 2.returns a function
# (in py functions are arguments)
# 1.
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("higher order function")
    print(text)


hello(loud)
hello(quiet)
# 2.return a funtion


def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide = divisor(4)
print(divide(10))
