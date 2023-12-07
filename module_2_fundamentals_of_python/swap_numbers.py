print("swap two number with temp variable:\n")
a = 20
b = 10
print("Before swap values are:","a=",a,"b=",b)
temp = a
a = b
b = temp
print("After swap values are:","a=",a,"b=",b)

print("\nswap two number without temp variable:\n")
a = 20
b = 10
print("Before swap values are:","a=",a,"b=",b)
a = a + b
b = a - b
a = a - b
print("After swap values are:","a=",a,"b=",b)
