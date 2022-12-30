def create_stack():
    """Creates an empty stack"""
    return []


def push_stack(item, stack):
    """Add item to the top of stack"""
    stack.append(item)


def pop_stack(stack):
    """Remove and return the item at the top of the stack"""
    return stack.pop()


def top_stack(stack):
    """Return the value of the item at the top of the stack
without removing it"""
    return stack[-1]


def is_empty_stack(stack):
    """Check whether the Stack is empty"""
    return stack == []
