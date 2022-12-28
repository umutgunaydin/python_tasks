# Write a recursive function named keep that is equivalent to built-in filter function
def keep(func, lis):
    if len(lis) == 0:
        return []
    if func(lis[0]):
        return [lis[0]] + keep(func, lis[1:])
    else:
        return keep(func, lis[1:])


print(keep(str.isdigit, ['1', 'abc', '23', '45', 'ceng', '111']))
