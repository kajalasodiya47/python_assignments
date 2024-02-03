'''
 Write a Python program to copy the contents of a file to another file
'''
# opens a file for reading
f = open("text_file2.txt","r")
c = f.read()
# opens a file for appending 
s = open("text_file3.txt","a")
s.write(c)
s.close()
