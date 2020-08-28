"""
Insertion between two nodes is a little bit complex to do.
There are two different approaches.

1. inserting after an existing node
2. inserting before an existing node
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

        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:  # if the head needs to removed...
            self.head = self.head.next  # then the head of our nodes is equal to whatever was up next (b)
            return

        previous_node = self.head  # initialize a previous_node variable THAT WILL BE UPDATED
        for node in self:
            if node.data == target_node_data:  # when we find our target...
                previous_node.next = node.next  # previous node's next becomes == next of the node we want to delete
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

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
llist.add_before("c", Node("ee"))
print(llist)
llist.remove_node("ee")
print(llist)