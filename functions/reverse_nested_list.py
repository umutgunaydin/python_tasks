# Write a function that reverses the elements inside the given list.
# If the elements inside the list also contain the list, reverse their elements as well

def reverse_list(l):
    if l == []:
        return []
    else:
        for i in l:
            if type(i) == list:
                i.reverse()
        return l[::-1]


sample = [[7, 6, 5], [4, 3], [2, 1]]
print(reverse_list(sample))
