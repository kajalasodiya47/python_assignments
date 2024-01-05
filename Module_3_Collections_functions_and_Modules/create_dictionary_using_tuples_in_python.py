# define function convert_dict with argument
def convert_dict(tup, dic):  
    #dict()  
    dic = dict(tup)  
    return dic

# tuple    
tuple_values = [("a", 1), ("b", 2), ("c", 3),("d", 4), ("e", 5), ("f", 6)]
# empty dictionary
res_dictionary = {}
# call the function convert_dict  
print ("The converted dictionary is: ", convert_dict(tuple_values,res_dictionary))  
