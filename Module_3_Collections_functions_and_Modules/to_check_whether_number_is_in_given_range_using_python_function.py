# define function "test_range" with argument num
def test_range(num):
    # check the number is in given range or not
    if num in range(1,5):
        print("Number is in given range")
    else:
        print("Number is outside the given range")
# call the test_range function with the argument 3
test_range(3)        
