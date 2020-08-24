"""
A second attempt at a linked list
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

llist = LinkedList()
print(llist)
first_node = Node("a")
llist.head = first_node
print(llist)
second_node = Node("b")
first_node.next = second_node
print(llist)
