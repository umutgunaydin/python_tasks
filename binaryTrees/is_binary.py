# Write a function named isbinary which takes a tree as an argument
# and returns True if the tree is a binary tree and returns False otherwise.
import myTree


def is_binary(tree):
    if len(tree) > 3:
        return False
    elif myTree.is_empty(tree):
        return True
    else:
        return is_binary(myTree.left(tree)) and is_binary(myTree.right(tree))


print(is_binary([1, [2, [20]], [3, [30]], [4, [40]]]))
print(is_binary([1, [2, [], []], [3, [], []]]))