# Write a function named check_mul() which will take a tree as its argument and checks the tree according to the
# following rule and returns True (obeys the rule) or False (does not obey the rule) Rule: Each node (except leaf
# nodes) are equal to the product of values of its child nodes. Note: Each node holds a number and the tree is a
# complete binary tree (each interior node has two children
import myTree


def check_mul(tree):
    if myTree.is_leaf(tree):
        return True
    else:
        return myTree.datum(tree) == myTree.left(tree)[0] * myTree.right(tree)[0] and check_mul(
            myTree.left(tree)) and check_mul(myTree.right(tree))


print(check_mul([15, [3, [], []], [5, [], []]]))
print(check_mul([7, [3, [], []], [5, [], []]]))
print(check_mul([-35, [7, [], []], [-5, [-1, [], []], [5, [], []]]]))
print(check_mul([72, [8, [4, [], []], [2, [-1, [], []], [-2, [], []]]], [9, [], []]]))
