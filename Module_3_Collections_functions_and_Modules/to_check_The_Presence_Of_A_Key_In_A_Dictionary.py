# dictionary
dict_1 = {"a": 1, "b":2, "c":3}
'''
get() method is a dictionary method that returns
the value of the associated key.
'''
if dict_1.get("a") is not None:
    print("Exists")
else:
    print("Does not exist")

