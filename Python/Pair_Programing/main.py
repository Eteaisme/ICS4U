class Point:
    # constructor, sets point to user coordinates, or default origin
    def __init__(self, x=0, y = 0):

    # getters:  get the x and y coordinates, returns a float
    def get_x(self):
        
    def get_y(self):

    # setters set the x and y coordinates
    def set_x (self, x):
        
    def set_y(self, y):

    # distance to another point, p, returns a float
    def dist_to_point(self, p):

    #distance to origin, returns a float
    def dist_to_origin(self):

    # return string representation of a point, i.e. coordinate pair (x,y)
    def __repr__(self):

    #return override of the equality boolean operator (true if x1==x2, y1==y2)
    def __eq__(self,other):
        


class Line:
    # constructor (default slope = 1 and intercept = 0)
    def __init__ (slope = 1, yint =0):

    # getters, return floats
    def get_slope (self):
        
    def get_yint(self):

    # setters
    def set_slope (self, slope):
        
    def set_yint (self, yint):

    # determine if two lines are parallel, return boolean
    def is_parallel (self,other):

    # determine if two lines are perpendicular to each other, return boolean
    def is_perpendicular (self, other):

    # determine if a point, p, is on the line return boolean
    def on_line(self, p):

    # return string representation of the slope and intercept of a line, e.g.
    # slope: 1.0 intercept: 0.0
    def __repr__(self):

    # return override of equality operator i.e. have the same slope, yint 
    def __eq__(self,other):
    

######## Test Code ####################3
p1 = Point()
p1.set_x(3)
p1.set_y(4)
print("Point 1: ", p1)
print("Distance to origin: ", p1.dist_to_origin())
p2 = Point(-1,-10)
print("p2 is at (", p2.get_x(),",",p2.get_y(),")")
print("Distance p1 to p2: ", p1.dist_to_point(p2))
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