"""
Real Python.com/linked-lists-python/
A second attempt at a linked list
"""


class LinkedList:
    """
    A class to represent your linked list.
    The only info needed to store for a linked list is where the list starts.
    The first node will be appointed as the head.
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:  # only do the following if a node has been appended to self.head
            nodes.append(node.data)  # append empty list with the node data
            node = node.next  # update the variable node with its value for next, which is the second node.
        nodes.append("None")
        return "->".join(nodes)


class Node:
    """
    The node stores two things: data and next.
    next is initialized as none.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()  # create an object
print(llist)
first_node = Node("a")  # create a node with data = "a"
llist.head = first_node  # appoint the first node as the head of LinkedList()
print(llist)  #
second_node = Node("b")  # create a second node
first_node.next = second_node  #
third_node = Node("c")
second_node.next = third_node
print(llist)
