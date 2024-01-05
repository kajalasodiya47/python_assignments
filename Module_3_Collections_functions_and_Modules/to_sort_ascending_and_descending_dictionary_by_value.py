#dictionary
my_dict = {'red': 'e', 'green': 'a',
           'black': 'z', 'white': 'c'}
print("Sorted dictionary is :")
# To sort dictionary by value using sorted() and get()
for w in sorted(my_dict, key = my_dict.get):
    print(w,my_dict[w])
