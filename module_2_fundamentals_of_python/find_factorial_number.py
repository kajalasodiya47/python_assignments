fact=1
# input the number to find factorial
num=int(input("Enter the number to find factorial:"))
'''
  for loop starts from 1 to (entered the num + 1)
'''  
for i in range(1,num+1):
    fact = fact * i   # in every iteration performs fact value multiply by i
print(fact)    # print factorial of given number  
