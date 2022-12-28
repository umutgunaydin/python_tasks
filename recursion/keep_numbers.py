# Write a recursive function named keep_numbers that takes a list as argument
# and returns a new list containing the numbers in the original list.
def keep_numbers(lis):
    if len(lis) == 0:
        return []
    elif type(lis[0]) == int or type(lis[0]) == float:
        return [lis[0]] + keep_numbers(lis[1:])
    else:
        return keep_numbers(lis[1:])


print(keep_numbers([4, "as", 3.2, "ad", 3]))
