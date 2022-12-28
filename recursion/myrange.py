# Write a recursive function named myrange that takes three integer arguments
# and returns a list of numbers. The function should work similar to the built-in range function.
# The first argument is the start number,
# the second is the end number and the third argument is the step, which is a positive integer.
def myrange(start, end, step):
    if start >= end:
        return []
    else:
        return [start] + myrange(start + step, end, step)


print(myrange(0, 11, 5))
