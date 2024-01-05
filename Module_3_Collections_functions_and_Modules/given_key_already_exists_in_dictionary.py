# dictionary
d = {'name': 'kajal', 'age': 22, 'subject': 'python'}

# Define a function 'is_key_present' 
def is_key_present(x):
    # use if-else, to check 'x' is a present in dictionary or not.
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

# Call the 'is_key_present' function with the argument 5 
is_key_present('mark')

# Call the 'is_key_present' function with the argument 9 
is_key_present('age') 
