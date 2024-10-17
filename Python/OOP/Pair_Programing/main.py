import math

class Point:
    # constructor, sets point to user coordinates, or default origin
    def __init__(self, x=0, y = 0):
        self.x = x
        self.y = y
    # getters:  get the x and y coordinates, returns a float
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y

    # setters set the x and y coordinates
    def setX (self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y

    # distance to another point, p, returns a float
    def distanceToPoint(self, point):
        distance = math.sqrt(((point.x - self.x)**2)+((point.y - self.y)**2))
        return distance
        
    #distance to origin, returns a float
    def distanceToOrigin(self):
        distance = math.sqrt(((self.x)**2)+((self.y)**2))
        return distance

    # return string representation of a point, i.e. coordinate pair (x,y)
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    #return override of the equality boolean operator (true if x1==x2, y1==y2)
    def __eq__(self,other):
        if ((self.x == other.x) and (self.y == other.y)):
            return True
        else: 
            return False
class Line:
    # constructor (default slope = 1 and intercept = 0)
    def __init__ (slope = 1, yint =0 ,vertical =False,xint =0):
        if vertical == True:
            self.xint = xint
        else:
            self.slope = slope
            self.yint = yint
        self.vertical = vertical

    # getters, return floats
    def getSlope (self):
        if self.vertical == True:
            return False
        else:
            return self.slope
    def getYIntercept(self):
        if self.vertical == True:
            return False
        else:
            return self.yint
    # setters
    def setSlope (self, slope):
        
    def setYIntercept (self, yint):

    # determine if two lines are parallel, return boolean
    def isParrallel (self,other):

    # determine if two lines are perpendicular to each other, return boolean
    def isPerpendicular(self, other):

    # determine if a point, p, is on the line return boolean
    def onLine(self, point):

    # return string representation of the slope and intercept of a line, e.g.
    # slope: 1.0 intercept: 0.0
    def __repr__(self):

    # return override of equality operator i.e. have the same slope, yint 
    def __eq__(self,other):

######## Test Code ####################3
p1 = Point()
p1.setX(3)
p1.setY(4)
print("Point 1: ", p1)
print("Distance to origin: ", p1.distanceToOrigin())
p2 = Point(-1,-10)
print("p2 is at (", p2.getX(),",",p2.getY(),")")
print("Distance p1 to p2: ", p1.distanceToPoint(p2))
print("Does p1=p2? ", p1==p2)

l1=Line()
l1.set_slope(-2)
l1.set_yint(10)
print(l1)
l2=Line(0.5,-3)
print("Does l1 =l2?: ", l1==l2)
print("Are l1 and l2 parallel? ", l1.is_parallel(l2))
print("Are l1 and l2 perpendicular? ", l2.is_perpendicular(l1))
print("Is p1 on l1? ", l1.on_line(p1))
print("Is p2 on l2? ", l2.on_line(p2))