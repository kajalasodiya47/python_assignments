'''
Write a Python program to count the number of lines in a text file

'''
# opens a file for reading
f = open("text_file.txt","r")
# read all the lines from a file
count = f.readlines()
# len() counts the number of lines in a text file
print(len(count))
