# create a list containing keys
keys = ['1', '2', '3']
# create a another list containing values
values = ['abc', 'xyz', 'pqr']
# Use the 'zip' function to pair each key name with its corresponding value 
# Then, use the 'dict' constructor to convert this list of tuples into a dictionary 
dictionary = dict(zip(keys,values))
print(dictionary)
