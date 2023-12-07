user_str = input("Enter a string : ")
res = {}
for key in user_str:
    res[key] = res.get(key,0) + 1
print(res)    
