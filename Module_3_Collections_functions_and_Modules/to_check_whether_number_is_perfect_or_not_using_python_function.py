# define function "check_perfect_number" with argument
def check_perfect_number(number):
    # initialize sum 
    sum = 0
    # Iterate through numbers from 1 to 'number - 1'
    for i in range(1,number):
        # to check 'i' is a factor of number
        if number % i == 0:
            sum += i
    return sum == number
# call the check_perfect_number() function with argument
print(check_perfect_number(28))
