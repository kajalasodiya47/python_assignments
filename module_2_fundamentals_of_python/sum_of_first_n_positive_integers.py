sum = 0
# input the number
num = int(input("Enter number : "))
'''
   for loop starts from 1 to entered num + 1
'''   
for i in range(1,num+1):
    sum = sum + i   # when every iteration performs, sum = sum + i
print("sum of first",num,"integers : ",sum)   # print the sum of first n positive integers  
