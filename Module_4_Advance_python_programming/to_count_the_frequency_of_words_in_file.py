'''
 Write a Python program to count the frequency of words in a file

'''
# import module
from collections import Counter
# opens a file for reading
f = open("text_file4.txt","r")
# through counter to count the frequency of words
fre_wrds = Counter(f.read().split())
print(fre_wrds)

