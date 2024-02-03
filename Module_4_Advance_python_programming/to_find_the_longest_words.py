'''
  Write a python program to find the longest words
  
'''
# Opens a file for reading text
f = open("text_file.txt","r")
#Split a string into a list where each word is a list item:
words = f.read().split()
# use max() to find the max from words
max_len = len(max(words,key=len))
# use for loop
# iterate through the words
for word in words:
    if len(word) == max_len:
       print(word)  
    
 
