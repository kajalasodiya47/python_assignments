# dictionary
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'d': 400, 'a': 500, 'c': 600}
# copy dict1 dictionary into combined_dict  dictionary
combined_dict = dict1.copy()
 
# add the values with common key
for key,value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value
         
print(combined_dict)

