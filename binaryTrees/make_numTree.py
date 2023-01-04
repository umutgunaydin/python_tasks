# Write a function named num_parts which will create a binary tree by using a single argument: a positive integer.
# The number will be the root of the final tree.
# The other nodes will be created by dividing the root into two values;
# if n is even, n/2; if n is odd, ((n-1)/2)+1 and (n-1)/2.

# In the final tree the following rules must hold:
# For each node, when values of children are added up, the result must give the value of this node.
# For each node, the child with a larger value must be at the left.
# Each leaf will have the value of 1.
import myTree


def num_parts(number):
    if number == 1:
        return [1]
    elif number % 2 == 0:
        return [int(number)] + [num_parts(number / 2)] + [num_parts(number / 2)]
    elif number % 2 == 1:
        return [int(number)] + [num_parts(((number - 1) / 2) + 1)] + [num_parts((number - 1) / 2)]


print(num_parts(8))
print(num_parts(7))
