# super()=Function used to give access to the methods of the parent class
# Returns a temp object of a parent class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)  # instead of repeating the assignment

    def area(self):
        return self.length*self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height  # only new attributes need to be initialized

    def volume(self):
        return self.height*self.width*self.length


square = Square(3, 3)
print(square.area())
cube = Cube(3, 3, 3)
print(cube.volume())
