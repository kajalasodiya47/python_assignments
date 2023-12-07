input_str = "The lyrics is not that poor!"
x = input_str.find('not')
y = input_str.find('poor')
if y > x:
   input_str = input_str.replace(input_str[x:y+4],'good')
   print(input_str)
else:
   print(input_str)
