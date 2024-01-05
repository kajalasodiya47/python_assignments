# list
my_list = [(1,3,4),(9,0,6),(2,6,9)]
# Use the 'zip' function with the '*' operator to unpack and zip the tuples
# to unzip a list of tuples into individual lists
result = list(zip(*my_list))
print(result)
