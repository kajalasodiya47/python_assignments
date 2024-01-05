def common_member(list1,list2):
    for item in list1:
        if item in list2:
           return True
        
list1 = [11,12,13,14,28]
list2 = [21,22,28,23,17]
print(common_member(list1,list2))
