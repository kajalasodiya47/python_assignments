# list
list1 = [5, 6, 3, 8, 2, 1, 7, 1]
# print original list
print("Original list is : ",list1)
# sublist
sub_list = [8, 2, 7]
# check for sublist in list
i = 0
result = False
for i in sub_list:
    if i in list1:
        i+=1
    if(i==len(sub_list)):
        result=True
# result
print("Is sublist present in list ? :",result)
