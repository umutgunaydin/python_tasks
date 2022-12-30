def createQueue():
    """Creates an empty queue"""
    return []


def pushQueue(item, queue):
    """Add item to the end of queue"""
    queue.append(item)


def popQueue(queue):
    """Remove and return the item at the front of the queue"""
    p = queue[0]
    del queue[0]
    return p


def topQueue(queue):
    """Return the value of the item at the front of the queue
without removing it"""
    return queue[0]


def isEmptyQueue(queue):
    """Check whether the Queue is empty"""
    return queue == []
