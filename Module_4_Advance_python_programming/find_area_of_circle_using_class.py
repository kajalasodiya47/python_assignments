'''
Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle

'''
# create a class named Circle
class Circle:
    # __init__() : call automatically when object of class is created
    def __init__(self,radius):
        self.radius = radius
        
    # define a method area_of_circle()
    def area_of_circle(self):
        area = 3.14 * self.radius * self.radius
        return area

    # define a method perimeter_of_circle()
    def perimeter_of_circle(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter
# object creation
O = Circle(4)
print("Area of circle : ",O.area_of_circle())
print("Perimeter of circle : ",O.perimeter_of_circle())

        
