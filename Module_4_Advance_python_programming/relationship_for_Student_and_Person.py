'''
  What relationship is appropriate for Student and Person?
  
  Ans :- In python, the relationship between 'Student' and 'Person' can be modeled using inheritance. 

'''
# define a class Person
class Person:
    # dunder method
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # member method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# define a another class Student        
class Student(Person):
    # dunder method
    def __init__(self,name,age,student_id):
        # super() function returns an object that represents the parent class
        super().__init__(name,age)
        self.student_id = student_id
    # member method
    def display_info(self):
        # super() function returns an object that represents the parent class
        super().display_info()
        print(f"Student ID : {self.student_id}")
# create a Person named class object
person = Person("Kajal",25)
# create a Student named class object
student = Student("Vyana",20,"123")
person.display_info()
student.display_info()
