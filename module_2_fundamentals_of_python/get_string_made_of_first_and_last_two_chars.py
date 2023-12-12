# input the string
str = input("Enter a string : ")
'''
  if string length is less than 2 returns the empty string and if string length is greater than 2 returns the first 2 and last 2 chars from a given string using slicing string
'''  
if len(str) < 2:
    result = ""
else:
    result = str[:2] + str[-2:]
# print the result    
print("Result:",result)    
