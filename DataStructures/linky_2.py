"""
Real Python.com/linked-lists-python/
"""

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next  # iterate based on the next

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