# enter string
user_str = input("Enter a string : ")
# empty dictionary
res = {}
# for loop
for key in user_str:
    '''
      use get(key,value) dictionary method to return the value with +1
    ''' 
    res[key] = res.get(key,0) + 1
print(res)    
