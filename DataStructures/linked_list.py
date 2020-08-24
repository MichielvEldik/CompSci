"""
Implementation of linked lists


"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None # points to the head of the linked list
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head) # use node class to create node object with data and self.head if there is any.
        self.head = node # self.head will become the node that we just created

    def print(self):
        if self.head is None: 
            print("Linked list is empty") # if you print before creating a self.head, then you have no linked list.
            return
        
        itr = self.head # if it's not blank. create a variable iterator and assign head to it. 
        llstr = '' # have something to print.

        while itr: # you are now following the link of your linked list, going through it one by one.
            llstr += str(itr.data) + '-->' # show connections between nodes.
            itr = itr.next # in the node, this is used to go to the next head. So you go from head to head to head to head to head. et cetera.
        print(llstr)



if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print()
