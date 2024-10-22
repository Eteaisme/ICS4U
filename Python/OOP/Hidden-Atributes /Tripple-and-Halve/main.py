"""
Write a class called TripleAndHalve that has a single hidden instance variable called number. This number should start at 1.

The class should have three methods:

triple, which multiplies number by 3.
halve, which divides number by 2 using integer division (//).
print_number, which simply prints the value of number to the screen.
Then, make an instance of this class. See if you can use a combination of calls to triple and halve to get number to be 7.


"""

class TripleAndHalve:
    def __init__(self):
        self.__number = 1

    def triple(self):
        self.__number *= 3

    def halve(self):
        self.__number = self.__number//2 

    def printNumber(self):
        print(self.__number)



n1 = TripleAndHalve()
n1.triple()
n1.triple()
n1.triple()
n1.triple()
n1.triple()

n1.halve()
n1.halve()
n1.halve()
n1.halve()
n1.halve()
n1.printNumber()


