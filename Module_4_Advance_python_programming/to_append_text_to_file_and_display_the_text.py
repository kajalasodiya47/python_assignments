'''
Write a Python program to append text to a file and display the text.

'''
# Opens a file for for appends text
f = open("text1_file.txt","a")
name = input("Enter name : ")
subject = input("Enter subject : ")
mark = input("Enter mark : ")
f.write(name)
f.write("\n"+subject)
f.write("\n"+mark)
f.close()
# Opens a file for for reading
f = open("text1_file.txt","r")
print(f.read())
