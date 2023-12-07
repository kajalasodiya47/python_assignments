user_str = input("Enter a string:")
if len(user_str) < 3:
    result = user_str
elif user_str.endswith('ing'):
    result = user_str + 'ly'
else:
    result = user_str + 'ing'
print("Result : ", result)    
