'''
Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle 

'''
# create a class named Rectangle
class Rectangle:
    # __init__() : call automatically when object of class is created
    def __init__(self,length,width):
        self.length = length
        self.width = width
    # define a method compute_area()
    def compute_area(self):
        area = self.length * self.width
        return area
# object creation
O = Rectangle(2,3)
print("Area of Rectangle is : ",O.compute_area())
