# Write a function named sum_tree that takes a binary tree consisted of integer datum as argument
# and returns the summation of its nodes.
import myTree


def sum_tree(tree):
    if myTree.is_empty(tree):
        return 0
    else:
        return myTree.datum(tree) + sum_tree(myTree.left(tree)) + sum_tree(myTree.right(tree))


tree2 = [1, [2, [3, [], []], []], [5, [], [6, [], []]]]
print(sum_tree(tree2))
