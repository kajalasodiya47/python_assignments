'''
 How will you compare two lists :-

 You can use the sort() method or the sorted() function to sort lists with the purpose of comparing

 them for equality.
 
'''

# sort() method example :

'''
The following example explains how to use the sort() method to sort and

compare lists for equality:

'''

l1 = [1,2,3,4,5]
l2 = [2,3,5,4,7]
l3 = [5,1,3,2,4]

print(l1.sort())
print(l2.sort())
print(l3.sort())

if l1 == l2:
    print("lists l1 and l2 are the same")
else:
    print("lists l1 and l2 are not the same")

if l1 == l3:
    print("lists l1 and l3 are the same")
else:
    print("lists l1 and l3 are not the same")    
