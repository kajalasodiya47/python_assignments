'''
How Do You Handle Exceptions With Try/Except/Finally In Python?
Explain with coding snippets.

Ans :-  Try, except and finally blocks are used for exception handling.
The try block which is contain code
The except block which is similar like catch and handle exception
The finally block which always invoke exception occur or not

'''
try:
    num = int(input("Enter a number : "))
    print(num*num)
except:
    print("Invalid input")
finally:    
    print("Thank you for using this application")
