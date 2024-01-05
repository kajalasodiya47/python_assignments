def count_strings(x):
    count = 0
    for str1 in x:  # give the one by one string from the list of strings when every iteration performs 
       '''
          use len() function to check the given string lentgh is greater than or eual too or not and
          compare the first and last character from a string is equal too or not
       '''   
       if len(str1) >= 2 and str1[0] == str1[-1]: 
            count += 1
    return count         
       
# list of strings    
my_list = ["pop","push","sun","radar","dad","mom"]
# call the count_strings() function
print("Number of strings with the same first and last character : ",count_strings(my_list))
