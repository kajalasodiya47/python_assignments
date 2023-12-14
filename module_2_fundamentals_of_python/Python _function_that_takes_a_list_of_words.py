def find_longest_word(*x):
  longest_word = max(x)  #returns the largest item 
  print("Longest word is : ",longest_word)  #print the longest word
  return len(longest_word)  # returns the length of longest word using len() function 

print("Length of the longest word is : ",find_longest_word("Apple","Orange","Banana","Watermelon"))




