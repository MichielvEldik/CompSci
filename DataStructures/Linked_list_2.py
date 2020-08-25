"""
Real Python.com/linked-lists-python/
Modified version of the linked list.
In this case, you pass in a list of nodes.
"""


class LinkedList:

    def __init__(self, nodes=None):  # gets initialized with a list of nodes
        self.head = None
        if nodes is not None:  # If there is at least one node passed to the class...
            node = Node(data=nodes.pop(0))  # pop first element in the list ("a") from nodes. assign a as "node"
            self.head = node  # make node ("a") the head of linked list.
            for elem in nodes:  # for every element in nodes ("a", "b", "c")
                node.next = Node(data=elem)  # node.next for ("a") is elem "b". ("a") so node.next = Node b
                node = node.next  # update the current node ("a") and make it equal to whatever is next ("b")

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return "->".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    """
    The node stores two things: data and next.
    next is initialized as none.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self): # what is exactly this class about?
        return self.data


llist = LinkedList(["a", "b", "c", "d"])
print(llist)