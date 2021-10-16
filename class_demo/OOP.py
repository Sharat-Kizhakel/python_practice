class Car:
    # self is passed automatically at the time of instantiation not needed to be passed explicitly
    # like a constructor in python
    # self refers to the object that we are currently workinng on

    wheels = 4  # class variable

    def __init__(self, make, model, year, color):
        self.make = make  # instance var:declared inside the constructor
        self.model = model  # instance var
        self.year = year  # instance var
        self.color = color  # instance var

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("The "+self.model+" car stopped")
