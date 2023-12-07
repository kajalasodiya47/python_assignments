n1 = 0
n2 = 1
n3 = n2 + n1
step = int(input("Enter the steps to print fibonacci series:"))
print("Fibonacci series:",n1,n2,n3,end=" ")
for i in range(1,step-2):
   n1 = n2
   n2 = n3
   n3 = n1 + n2
   print(n3,end=" ")
