'''
when is the finally block executed?

Ans :- The finally block in a try-except-finally statement is always executed, regardless of whether an
exception is raised or not.

'''

try:
  num = int(input("Enter a number : "))
except:
  print("Invalid input")
else:
  print(num*num)
finally:
  print("Thank you for using this application")
