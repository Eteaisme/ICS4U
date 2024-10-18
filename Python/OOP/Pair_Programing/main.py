import numpy as np            
import matplotlib.pyplot as plot 
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

    def plotPoint(self):
    #gets scale of graph
        tickScale = 0
        isDivisable = True
        graphScale = 20
        if(self.x > self.y):
            graphScale = self.x*2 
        else: 
            graphScale = self.y*2
        xMin, xMax, yMin, yMax = -abs(graphScale), graphScale, -abs(graphScale), graphScale

        #getsTickScale
        while (isDivisable == True):
            tickScale = graphScale
            if((tickScale% 2) == 0):
                tickScale = tickScale%2
                print(tickScale)
            else:
                isDivisable = False
                


        
        #Plot points
        fig, ax = plot.subplots(figsize=(10, 10))
        ax.scatter(self.x, self.y, c="b")

        #Create axes
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero') 
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
        ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
        xTicks = np.arange(xMin, xMax+1, tickScale)
        yTicks = np.arange(yMin, yMax+1, tickScale)
        ax.set_xticks(xTicks[xTicks!= 0])
        ax.set_yticks(yTicks[yTicks != 0])

        plot.show()






    # return string representation of a point, i.e. coordinate pair (x,y)
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    #return override of the equality boolean operator (true if x1==x2, y1==y2)
    def __eq__(self,other):
        if ((self.x == other.x) and (self.y == other.y)):
            return True
        else: 
            return False
"""
class Line:
    # constructor (default slope = 1 and intercept = 0)
    def __init__ (slope = 1, yint =0):

    # getters, return floats
    def getSlope (self):
        
    def getYIntercept(self):

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
"""
######## Test Code ####################3
p1 = Point()
p1.setX(8)
p1.setY(5)
print("Point 1: ", p1)
print("Distance to origin: ", p1.distanceToOrigin())
p2 = Point(-1,-10)
print("p2 is at (", p2.getX(),",",p2.getY(),")")
print("Distance p1 to p2: ", p1.distanceToPoint(p2))
print("Does p1=p2? ", p1==p2)
p1.plotPoint()