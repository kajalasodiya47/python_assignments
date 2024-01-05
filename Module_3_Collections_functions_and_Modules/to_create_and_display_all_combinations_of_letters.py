my_dict = {'1': ['a', 'b'],'2': ['c', 'd']}
for key1 in my_dict:
    for key2 in my_dict:
        if key1 != key2:
            for value1 in my_dict[key1]:
                for value2 in my_dict[key2]:
                    print(value2)
