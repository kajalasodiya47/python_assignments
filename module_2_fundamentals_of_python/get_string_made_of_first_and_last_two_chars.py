str = input("Enter a string : ")
if len(str) < 2:
    result = ""
else:
    result = str[:2] + str[-2:]
    
print("Result:",result)    
