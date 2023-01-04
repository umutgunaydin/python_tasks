# Write a function named max_depth which takes a tree as an argument and returns the depth of the deepest leaf.
import myTree


def max_depth(tree):
    if myTree.is_leaf(tree):
        return 1
    else:
        if max_depth(myTree.left(tree)) >= max_depth(myTree.right(tree)):
            return 1 + max_depth(myTree.left(tree))
        else:
            return 1 + max_depth(myTree.right(tree))


print(max_depth([1, [2, [], []], [3, [], []]]))
print(max_depth([1, [2, [6, [], []], [7, [8, [], []], [9, [], []]]], [3, [4, [], []], [5, [], []]]]))
print(max_depth([1, [2, [], []], [3, [4, [], []], [5, [], []]]]))
