# define function is_string_palindrome with argument
def is_string_palindrome(input_str):
    # to check given string and reverse string is palindrome
    if input_str == input_str[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome")
# string
input_str = "madam"
# call the function is_string_palindrome with argument
is_string_palindrome(input_str)
