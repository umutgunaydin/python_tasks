# You need to schedule orders for a firm.
# The firm can do a single order a day and do them on a first-come first-served basis.
# Write a function named schedule which takes the order queue which contains the customer informations
# and the requested deadlines for the orders
# and returns the list of orders that cannot be completed until or during the requested deadline
import queue


def schedule(q):
    lis = []
    day = 1
    for i in range(len(q)):
        if day > q[i][0]:
            lis.append((q[i][1], q[i][0]))
        else:
            day += 1
    print(lis)


q = queue.createQueue()
queue.pushQueue((1, "John"), q)
queue.pushQueue((5, "George"), q)
queue.pushQueue((1, "Lucy"), q)
queue.pushQueue((2, "Arnold"), q)
queue.pushQueue((3, "William"), q)
queue.pushQueue((4, "Claude"), q)
schedule(q)
