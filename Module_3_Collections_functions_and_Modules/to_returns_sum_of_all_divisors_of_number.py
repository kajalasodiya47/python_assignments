# define function sum_of_all_divs with argument
def sum_of_all_divs(num):
    # list item
    divisors = [1]
    # use for loop 
    for i in range(2,num):
        # check entered num is divisble by i == 0
        if(num % i) == 0:
            # append i in every iteration
            divisors.append(i)
    # use sum(), to sum of all list divisors item        
    return sum(divisors)

print("Sum of all divisors of number : ",sum_of_all_divs(8))
