class Car:
    num_doors = 4

    def __init__(self):
        self.num_wheels = 4

c = Car()
c.num_doors = 6
print(c.num_doors)
print(Car.num_doors)