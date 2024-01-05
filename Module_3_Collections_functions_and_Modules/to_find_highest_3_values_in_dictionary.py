my_dict = {'a': 22, 'b': 10, 'c': 45,
        'd': 10, 'e': 12, 'f': 20}
print(my_dict, "\n")
# convert dictionary into a list
x=list(my_dict.values())
# sort the list in descending order
x.sort(reverse=True)
# get first 3 highest values
x=x[:3]
for i in x:
    for j in my_dict.keys():
        if(my_dict[j]==i):
            print(j+" : ",my_dict[j])
