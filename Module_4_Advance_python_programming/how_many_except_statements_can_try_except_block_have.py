'''
 How many except statements can a try-except block have? Name Some built-in exception classes:
 
 Ans :- A try-except block can have multiple except caluses to handle different types of exceptions.
 You can catch multiple exception types by listing them inside separate except blocks.

 Some built-in exception classes:-
 1) ValueError
 2) TypeError
 3) ZeroDivisionError
 4) FileNotFoundError
 5) IndexError
     
'''

try:
  num1 = int(input("Enter a number 1 : "))
  num2 = int(input("Enter a number 2 : "))
  ans = num1 / num2
  print(ans)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as z:
    print(z)
    
  
  
