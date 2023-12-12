# swap two numbers with temp variable

print("swap two number with temp variable:\n")
a = 20
b = 10
print("Before swap values are:","a=",a,"b=",b)
temp = a  # value of a variable assigned to temp variable
a = b     # and value of b variable assigned to a variable
b = temp  # and then after value of temp variable assigned to b variable

# after swapping the values are:
print("After swap values are:","a=",a,"b=",b)



# swap two numbers without temp variable

print("\nswap two number without temp variable:\n")
a = 20
b = 10
print("Before swap values are:","a=",a,"b=",b)
a = a + b  # addition of a and b variable, and the addition assigned to a variable
b = a - b  # and subtraction of a and b variable, and the subtraction assigned to b variable
a = a - b  # and then after subtraction of a and b variable, and the subtraction assigned to a variable

# after swapping the values are:
print("After swap values are:","a=",a,"b=",b)
