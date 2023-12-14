'''
     use if else conditional statements,
     if length of the given string is modulo by 4 is eual to zero
     then reverses a string, otherwise returns a given string
''' 
def reverse_string(str1):
    if len(str1) % 4 == 0:  
       return str1[::-1]
    else:
       return str1 
     
# string         
str1 = "helloall"
print(reverse_string(str1))  #call the reverse_string() function
