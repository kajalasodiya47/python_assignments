'''
   use slicing add the substring "all" in the middle of the string
'''   
def insert_string(str1):
 str2 = "all"    
 str_result = str1[:7]+str2+" "+str1[7:]
 return str_result

# string
str1 = "hello, world!"
print(insert_string(str1))  # call the insert_string() function
