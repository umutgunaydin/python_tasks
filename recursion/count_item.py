# Write a recursive function named count_item that takes an object
# and a list as arguments returns the number of occurrences of the object in the list.
def count_item(item, lis):
    if len(lis) == 0:
        return 0
    elif item == lis[0]:
        return 1 + count_item(item, lis[1:])
    else:
        return count_item(item, lis[1:])


print(count_item(1, [3, 5, 7, 3, 21, 1, 1, 1, 3, 1]))
