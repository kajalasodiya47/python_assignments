# tuple item
my_tuple = (1,2,3,4,1,6,7,7,4)
# empty list
my_list = []
'''
  use for loop
  count() function count the items, is greater than one or not in tuple,
  if items is repeated
  than append in my_list
'''  
for i in my_tuple:
    if my_tuple.count(i) > 1:
        my_list.append(i)
    else:
        continue
'''
  use for loop
  if item in tuple is repeated
  remove() method removes the first occurance of the repeated item
'''    
for l in my_list:
    if my_list.count(l) > 1:
        my_list.remove(l)
        
print(my_tuple)
print("Repeated items of a tuple : ",my_list)
