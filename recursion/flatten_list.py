# Write a function that flattens a list.
# Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data.


def flatten(l):
    if l == []:
        return []
    elif type(l) != list:
        return [l]
    elif len(l) == 1:
        if type(l[0]) != list:
            return [l[0]]
        else:
            flatten(l[0])

    return flatten(l[0]) + flatten(l[1:])


sample_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(sample_list))
