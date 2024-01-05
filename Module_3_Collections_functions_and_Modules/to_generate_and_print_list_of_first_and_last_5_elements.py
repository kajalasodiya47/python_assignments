# define function "values"
def values():
    # empty list
    my_list = []
    # Loop from 1 to 30 (inclusive)
    for i in range(1,31):
        # Calculate the square of 'i' and append it to the list 'l'
        my_list.append(i**2)
    print(my_list[:5])
    print(my_list[-5:])
# call values function
values()    
