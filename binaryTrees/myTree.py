def datum(tree):
    return tree[0]


def left(tree):
    return tree[1]


def right(tree):
    return tree[2]


def is_empty(tree):
    return tree == []


def is_leaf(tree):
    return left(tree) == [] and right(tree) == []


def make_node(datum, left=[], right=[]):
    return [datum, left, right]
