'''
Write a Python program to read first n lines of a file.

'''
# input number
n = int(input("Enter number of lines : "))
# opens a file for reading
f = open("text_file.txt","r")
for i in range(1,n+1):
    print(f.readline())


