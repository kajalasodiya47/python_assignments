'''
How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

Ans :- To create a class, use the class keyword
Self represents the instance of the class. By using the "self" we can access the attributes and methods
of the class in python

'''

class Sample:
    # class member
    num = 20
    # class method
    def add(self):
        print("Addition : ",self.num+10)
        
    def mul(self):
        print("Multiplication : ",self.num*2)
# object creation
s = Sample()
s.add()
s.mul()
