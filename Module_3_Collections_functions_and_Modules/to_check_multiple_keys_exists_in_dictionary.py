# dictionary
d = {'name': 'kajal', 'age': 22, 'subject': 'python','a':2,'c':5}
key1 = set(['name','a','c'])
key2 = set(['b','marks','grade'])
# use issubset() method Return True if all items in set key1 are present in dictionary d:
print(key1.issubset(d.keys()))
print(key2.issubset(d.keys()))

