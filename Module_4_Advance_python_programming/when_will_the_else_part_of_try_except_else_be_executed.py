'''
 When will the else part of try-except-else be executed?
 
 Ans :- In a try-except-else block in Python, the else block is executed if and only if the try block completes without raising any exceptions.
 This means that if no exceptions occur during the execution of the code inside the try block,
 the control flows to the else block.

'''

try:
    num = int(input("Enter a number : "))
except:
    print("Invalid input")
else:
    print(num*num)
