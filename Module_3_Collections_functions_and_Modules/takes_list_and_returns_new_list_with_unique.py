def new_list(list1):
 #get unique values from a list   
 list2 = list(dict.fromkeys(list1))
 print(list2)
 
#list item    
list1 = [1,2,3,4,5,2,1,6]
new_list(list1)
