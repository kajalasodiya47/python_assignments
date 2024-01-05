# list of tuples
my_list = [(11,12,13),(14,15,16),(),(17,18,19)]
'''
 use for loop,
 in for loop use if-else statements
 use len() function, if length of tuple == 0,
 then remove the particular tuple

'''
for t in my_list:
    if len(t) == 0:
        my_list.remove(t)

print(my_list)        
