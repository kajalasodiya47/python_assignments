# enter string
user_str = input("Enter a string:")
'''
  use ladder else if conditional statement 
  
''' 
# if the string length of the given string is less than 3, leave it unchanged
if len(user_str) < 3:
    result = user_str
#  string already ends with 'ing' then add 'ly'    
elif user_str.endswith('ing'):
    result = user_str + 'ly'
# add 'ing' at the end of a given string    
else:
    result = user_str + 'ing'
# print the result    
print("Result : ", result)    
