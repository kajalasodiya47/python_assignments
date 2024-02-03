'''
Write python program that user to enter only odd numbers, else will
raise an exception.

'''


try:
  num = int(input("Enter a odd number : "))
  # if condition returns False, AssertionError is raised:
  assert num %2 != 0
  print("odd number")
except:
   print("Please enter odd number") 

