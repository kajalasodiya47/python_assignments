'''
 Write a Python program to write a list to a file

'''
# opens a file for writing
f = open("text_file2.txt","w")
# list
list = ["kajal","ruchi","niyati","vyana"]
# iterate over the list
for item in list:
    f.write(item+"\n")
f.close()    
