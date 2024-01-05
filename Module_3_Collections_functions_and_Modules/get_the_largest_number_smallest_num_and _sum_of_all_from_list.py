def list_operations():
    sum_result = 0
    list1 = [23,12,14,34,65]
    largest_num = max(list1)  # find max number from a list
    smallest_num = min(list1)  # find min number from a list
    print(list1)                
    print("Largest number is : ",largest_num)
    print("Smallest number is : ",smallest_num)
    for i in list1:
        sum_result = sum_result + i     # when every iteration performs, sum_result = sum_result + i
    return sum_result

print("Sum of all from a list : ",list_operations())   # call the list_operations() function

