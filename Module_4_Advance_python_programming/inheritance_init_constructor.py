'''
Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?

Ans :-

Inheritance :- Ability to adapt the behaviour of parent class to child class
Types of Inheritance :-
1) Single Level Inheritance
2) Multiple Inhritance
3) Multi Level Inheritance
4) Heirarchical Inheritance
5) Hybrid Inheritance

init :- init method is also called dunder/magic method.
        init method call automatically when object of class is created.

Constructor :- Constructors are generally used for instantiating an object. The task of constructors
is to initialize(assign values) to the data members of the class when an object ot the class is created.
In Python the __init__() method is called the constructor and is always called when an object is created.
'''

print("---------Single Level Inheritance---------")
# create a class named A
class A:
    # dunder method
    def __init__(self,x,y):
        self.n1 = x
        self.n2 = y
    # class method 
    def displayA(self):
        print("number 1 is : ",self.n1,"and number 2 is : ",self.n2)
# create a another class named B
class B(A):
    # class method
    def displayB(self):
        print("Hello from child class")
# object creation
b1 = B(10,12)
b1.displayA()
b1.displayB()

print("----------Multiple Inheritance-----------")
#create a class named A
class A:
    # dunder method
    def __init__(self,stu_name,stu_age):
        self.n = stu_name
        self.a = stu_age
    # class method
    def displayS(self):
        print("Student details :- ")
        print("Student name : ",self.n)
        print("student age : ",self.a)
# create a another class named B
class B(A):
    # class method
    def input(self,stu_sub,stu_mark):
        self.s = stu_sub
        self.m = stu_mark
    # class method
    def displaySt(self):
        print("Student subject : ",self.s)
        print("student mark : ",self.m)
# create a another class named C        
class C(B,A):
    # class method
    def displayD(self):
          print("End")
# Object creation          
O = C("kajal",20)
O.displayS()
O.input("Maths",80)
O.displaySt()
O.displayD()

print("----------Multilevel Inheritance-----------")
#create a class named A
class A:
    # dunder method
    def __init__(self,stu_name,stu_age):
        self.n = stu_name
        self.a = stu_age
    # class method
    def displayS(self):
        print("Student details :- ")
        print("Student name : ",self.n)
        print("student age : ",self.a)
#create a another class named B
class B(A):
    # class method 
    def input(self,stu_sub,stu_mark):
         self.s = stu_sub
         self.m = stu_mark
    # class method
    def displaySt(self):
        print("Student name : ",self.s)
        print("student age : ",self.m)
#create a another class named C        
class C(B):
    # class method
    def displayC(self):
          print("End")
# object creation
O = C("kajal",22)
O.displayS()
O.input("Maths",85)
O.displaySt()
O.displayC()

print("----------Heirarchical Inheritance-----------")
#create a class named A
class A:
    # dunder method
    def __init__(self,stu_name):
        self.n = stu_name
    # class method    
    def displayS(self):
        print("Student details :- ")
        print("Student name : ",self.n)
#create a another class named B        
class B(A):
    # class method 
    def input(self,stu_age):
         self.a = stu_age
    # class method     
    def displaySt(self):
        print("student age : ",self.a)
#create a another class named C        
class C(A):
    # class method 
    def displayC(self):
          print("End")
# object creation          
c = C("kajal")
c.displayS()
c.displayC()
b = B("vyana")
b.displayS()
b.input(23)
b.displaySt()

print("----------Hybrid Inheritance-----------")
#create a class named A
class A:
    #dunder method
    def __init__(self,stu_name):
        self.n = stu_name
    #class method
    def displayA(self):
        print("Student details :-")
        print("Student name : ",self.n)
#create a another class named B         
class B(A):
    def input(self,stu_age):
        self.a = stu_age

    def displayB(self):
        print("Student age : ",self.a)
#create a another class named C         
class C(B):
    def inputc(self,stu_sub):
        self.s = stu_sub

    def displayC(self):
        print("Student subject : ",self.s)
#create a another class named D         
class D(A):
    def inputd(self,stu_marks):
        self.m = stu_marks

    def displayD(self):
        print("Student marks : ",self.m)
#create a another class named E         
class E(B,D):
    def inpute(self,stu_grd):
        self.g = stu_grd

    def displayE(self):
        print("Student grade : ",self.g)
# create class E object e through the get details of class A, B, D
e = E("Kajal")
e.displayA()
e.input(22)
e.displayB()
e.inputd(85)
e.displayD()
e.inpute("A")
e.displayE()
# create class B object b through the get details of class A
b = B("vyana")
b.displayA()
b.input(20)
b.displayB()
# create class C object c through the get details of class A, B
c = C("Ruchi")
c.displayA()
c.input(25)
c.displayB()
c.inputc("Maths")
c.displayC()
# create class C object c through the get details of class A
d = D("janvi")
d.displayA()
    
        
        



        
        
