# dictionary with same values
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
unique_values = set()

for value in my_dict.values():
    unique_values.add(value)

unique_values_list = list(unique_values)


print("Original Dictionary : ",my_dict)
print("Unique values list are : ",unique_values_list)
