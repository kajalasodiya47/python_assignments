'''
Can one block of except statements handle multiple exception?

Ans:- Yes, a single except block in a try-except statement in python, can handle multiple exceptions.
    You can specify multiple exception types in a tuple within a single except block.


'''

try:
  num1 = int(input("Enter a number 1 : "))
  num2 = int(input("Enter a number 2 : "))
  ans = num1 / num2
  print(ans)
except (ValueError,ZeroDivisionError) as e:
  print(e)
 
    

