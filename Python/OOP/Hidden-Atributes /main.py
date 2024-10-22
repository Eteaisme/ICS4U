class Rectangle:
    __numberOfEvenRectangles = 0
    
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

        if(self.getArea()%2 == 0):
            Rectangle.__numberOfEvenRectangles += 1
    
    
    def getArea(self):
        return self.length * self.width

    def getEvenRectangeles():
        return Rectangle.__numberOfEvenRectangles



    def __repr__(self):
        return "rectangle with length: " + str(self.length) \
            + " and width: " + str(self.width)


r1 = Rectangle(2, 6)
print(r1)
print(r1.getArea())


r2 = Rectangle(3, 5)
print(r2)
print(r2.getArea())

print(Rectangle.getEvenRectangeles())
r3 = Rectangle(4, 15)
print(Rectangle.getEvenRectangeles())