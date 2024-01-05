# string
input_str = "w3resource"
# empty dictionary
dict1 = {}
# use for loop iterate through the character
for letter in input_str:
    # use get(key,value) dictionary method to return the value with +1 
    dict1[letter] = dict1.get(letter,0) + 1
print(dict1)    
