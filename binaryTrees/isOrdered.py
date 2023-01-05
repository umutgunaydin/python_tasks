# Write a function named is_ordered which takes a binary tree as an argument
# and returns True if the tree is in a special form and returns False otherwise.
# This special form hold the following property:
# For each node; the datum of the left child must be less than the datum of the node
# and the datum of the right child must be greater than the datum of the node.
import myTree


def is_ordered(tree):
    if myTree.is_leaf(tree):
        return True
    else:
        return myTree.left(tree)[0] < myTree.datum(tree) < myTree.right(tree)[0] and is_ordered(
            myTree.left(tree)) and is_ordered(myTree.right(tree))


print(is_ordered([1, [2, [], []], [3, [], []]]))
print(is_ordered([2, [1, [], []], [4, [3, [], []], [7, [], []]]]))
