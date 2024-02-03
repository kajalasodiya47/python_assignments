'''
  What relationship is appropriate for Course and Faculty?

  Ans :- In python, you can establish a relationship between a course and faculty using object oriented
  programming concepts such as classes and attributes.

  One common way to represent this relationship is through composition or aggregation.  
  
'''
# define a class Faculty
class Faculty:
    # dunder method
    def __init__(self,name,department):
        self.name = name
        self.department = department
    # call automatically & return string when object is created
    def __str__(self):
        return f"name : {self.name}, Department: {self.department}"
# define a another class Course
class Course:
    # dunder method
    def __init__(self,c_name,faculty):
        self.c_name = c_name
        self.faculty = faculty
    # call automatically & return string when object is created
    def __str__(self):
        return f"Title : {self.c_name}, Faculty: {self.faculty}"
# create a faculty named class object 
fact_name = Faculty("Kajal","Python")
# create a course named class object 
course_name = Course("Python",fact_name)
print(course_name)

