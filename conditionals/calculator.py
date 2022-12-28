# Write a function named calculate that takes a list containing an operator
# and numbers as argument and returns the result of the operation
# Operations: 'add', 'minus', 'mult', 'div', 'min', 'max' (each takes two arguments)
def calculate(lis):
    if lis[0] == "add":
        return lis[1] + lis[2]
    elif lis[0] == "minus":
        return lis[1] - lis[2]
    elif lis[0] == "mult":
        return lis[1] * lis[2]
    elif lis[0] == "div":
        return lis[1] / lis[2]
    elif lis[0] == "min":
        if lis[1] > lis[2]:
            return lis[2]
        else:
            return lis[1]
    elif lis[0] == "max":
        if lis[1] > lis[2]:
            return lis[1]
        else:
            return lis[2]


print(calculate(['minus', 5, 7]))
