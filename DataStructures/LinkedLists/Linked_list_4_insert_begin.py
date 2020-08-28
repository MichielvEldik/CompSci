"""
Real Python.com/linked-lists-python/

The thing you have to remember is that you should not approach it like you would a list.
A linked list is not a list, it's a series of objects pointing to eah other and a print function that
makes use of that.

Time complexity:
It's easy to insert a node at the beginning, you always know which node is first!

"""


class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node):
        node.next = self.head  # node 'e' {Node} will get a next that is equivalent to current head ('a')
        self.head = node  # the current head ('a') is replaced by e with a as next.

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head  # this is now 'e'
        nodes = []  # empty list holder

        while node is not None:  # iterate until the end
            nodes.append(node.data)  # append empty list with node
            node = node.next  # update node variable. node = node.next

        nodes.append("None")
        return "->".join(nodes)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList(["a", "b", "c", "d"])
print(llist)
llist.add_first((Node("e")))
print(llist)