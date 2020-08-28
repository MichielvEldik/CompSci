"""
Real Python.com/linked-lists-python/
"""


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node  # this is the point where self.head != None anymore, this triggers repr method!!!!!!
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:  # because all of a sudden, a has become self.head, this sequence gets triggered
            nodes.append(node.data)  # nodes gets appended with the data of Node a, 'a'
            node = node.next  # node.next is b, so now the loop goes again. nodes.append(node.data) 'b', et cetera

        nodes.append("None")  # always end with None
        return "->".join(nodes)  # when print, return the nodes list as a string joined by -> arrows.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList(["a", "b", "c", "d"])
print(llist)
