# input 1st, 2nd and 3rd number
num1 = int(input("Enter 1st value : "))
num2 = int(input("Enter 2nd value : "))
num3 = int(input("Enter 3rd value : "))
'''
  if atleast 2 numbers are equal, sum will be zero otherwise performs the addition of given three numbers
'''  
if(num1 == num2 or num2 == num3 or num1 == num3):
    sum = 0
    print("sum : ",sum)
else:
    sum = num1+num2+num3
    print("sum : ",sum)
