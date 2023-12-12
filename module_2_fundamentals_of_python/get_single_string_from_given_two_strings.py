str1 = "kajal"
str2 = "asodiya"
x = str2[:1]+str1[1:]  #get the first character of str2 and get all the characters of str1 except first charcater 
y = str1[:1]+str2[1:]  #get the first character of str1 and get all the characters of str2 except first charcater
str3 = x +" "+y    # concates the x and y with space
print(str3)
