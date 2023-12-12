# string msg
input_str = "The lyrics is not that poor!"
'''
  find() method find the first occurrence of not and poor substring
'''  
x = input_str.find('not')
y = input_str.find('poor')
'''
   if poor substring first occurrence greater than not substring first occurrence replace the whole 'not'...'poor' substring with 'good otherwise returns the same as string
'''   
if y > x:  
   input_str = input_str.replace(input_str[x:y+4],'good') # replace method replaces the whole 'not'...'poor' substring with 'good
   print(input_str)
else:
   print(input_str)
