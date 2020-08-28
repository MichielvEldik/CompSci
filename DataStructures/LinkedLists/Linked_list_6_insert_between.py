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

        for node in self:  # the for loop is uses our __iter__ method. this will go through all nodes based on next
            if node.data == target_node_data:  # once the node.data == target-node data...
                new_node.next = node.next  # the next of our new node is whatever was originally next for the node
                node.next = new_node  # the next of original node is equal to our new node to complete the connection
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:  # if the target node == the first node of our sequence, we can use our
            return self.add_first(new_node)  # add_first method. No need to overcomplicate things!

        prev_node = self.head  # keep track of prev_node, this is just the starting point, it will get updated
        for node in self:  # for all nodes using our __iter__ method...
            if node.data == target_node_data:  # if we find a match at some point throughout the iteration...
                prev_node.next = new_node  # previous node's next will be equal to the new node
                new_node.next = node  # new node's next will be equal to node 
                return
            prev_node = node  # update previous node

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
#print(llist)
#llist.add_first((Node("e")))
#print(llist)
#llist.add_last(Node("z"))
#print(llist)
#llist.add_after("c", Node("cc"))
#print(llist)
llist.add_before("c", Node("ee"))
print(llist)
