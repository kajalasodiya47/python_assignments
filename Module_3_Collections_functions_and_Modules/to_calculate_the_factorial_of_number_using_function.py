# define function find_factorial with argument
def find_factorial(number):
    #check if the number is 0
    if number == 0:
        return 1
    else:
        # If 'n' is not 0, recursively call the 'factorial' function with (n-1) and multiply it with 'n'
        return number * find_factorial(number - 1)

# enter the number to find the factorial
number = int(input("Enter the number to find the factorial : "))
# call the find_factorial function
print("Factorial of a given number : ",find_factorial(number))
