str1 = "kajal"
str2 = "asodiya"
x = str2[:2]+str1[2:]  #get the first two characters of str2 and get all the characters of str1 except first two charcaters using slicing the strings
y = str1[:2]+str2[2:]  #get the first two characters of str1 and get all the characters of str2 except first two charcaters using slicing the strings
str3 = x +" "+y    # concates the x and y with space
print(str3)
