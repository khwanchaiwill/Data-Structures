class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    



# ll = Node(1)
# ll.set_next(Node(2))   
# ll.next.set_next(Node(3))
# ll.next.next.set_next(Node(4))
# ll.next.next.next.set_next(Node(5))
