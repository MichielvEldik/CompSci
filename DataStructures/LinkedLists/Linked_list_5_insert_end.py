"""
Inserting a node at the end is not as easy as inserting it at the beginning.
Why? You don't know which node is last! You have to go through all nodes to find out which one is last.
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
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:  # you want to traverse the whole list until you reach the end
            pass                   # that is until the for loop raises a StopIteration exception
        current_node.next = node  # next, the node that you are currently on will have None as next.
                                  # current_node.next = node will make sure that our imputed node will be seen as next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

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


llist = LinkedList(["a", "b", "c", "d"])
print(llist)
llist.add_first((Node("e")))
print(llist)
llist.add_last(Node("z"))
print(llist)
