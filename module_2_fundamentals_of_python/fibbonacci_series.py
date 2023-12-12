# displays the first two terms which is always 0 and 1
n1 = 0
n2 = 1
# third term is sum of first and second term
n3 = n2 + n1
# enter how many steps to continue with fibonacci series
step = int(input("Enter the steps to print fibonacci series:"))
# print first, second and third term
print("Fibonacci series:",n1,n2,n3,end=" ")
'''
 loop starts from 1 to (the steps entered - 2) because n1,n2,n3 are already printed
''' 
for i in range(1,step-2):
   n1 = n2  # value of n2 term assigned to n1 term
   n2 = n3  # value of n3 term assigned to n2 term
   n3 = n1 + n2  # sum of n1 and n2 term stored to n3 term
   print(n3,end=" ") # print n3 term 
