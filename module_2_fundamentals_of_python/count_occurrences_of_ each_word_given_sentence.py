# string
str1 = "To change the overall look your document. To change the look available in the gallery"
# empty dict() constructor
result = dict()
# split() method splits string into a list
word = str1.split(" ")

for key in word:
    result[key] = result.get(key,0) + 1
print(result) 
