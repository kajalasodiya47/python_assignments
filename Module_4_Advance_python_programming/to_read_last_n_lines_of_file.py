'''
Write a Python program to read last n lines of a file

'''
# input number
n = int(input("Enter number of lines to read last n lines of a file : "))
# opens a file for reading
f = open("text_file.txt","r")
lines = f.readlines()
last_lines = lines[-n:]
for line in last_lines: 
	print(line) 
