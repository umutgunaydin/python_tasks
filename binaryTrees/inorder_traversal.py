# Write a function named inorder which traverses a binary tree in-order.
import myTree


def inorder(tree):

    if myTree.is_empty(tree):
        return []
    else:
        return inorder(myTree.left(tree)) + [myTree.datum(tree)] + inorder(myTree.right(tree))


print(inorder([1, [2, [3, [], []], [4, [], []]], [5, [6, [], []], [7, [], []]]]))
