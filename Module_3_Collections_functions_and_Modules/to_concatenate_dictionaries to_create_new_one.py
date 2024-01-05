# dictionary 
dict1 = {1:11,2:12}
dict2 = {6:16,7:17}
dict3 = {}
# update() method updates the dictionary with the items from a given argument 
for d in (dict1,dict2,dict3):
    dict3.update(d)

print(dict3)    
