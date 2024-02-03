'''
Write a Python program to read a file line by line store it into a variable. 

'''

f = open("text_file.txt","r")
# Create an empty list
lines = []
# Iterate over the lines of file
for line in f:
    # Remove the newline character at the end of the line
    line = line.strip()
    # Append the line to the list
    lines.append(line)
# store it into a variables    
a,b,c,d = lines
print(a)
print(b)
print(c)
print(d)
