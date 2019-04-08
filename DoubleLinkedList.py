__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "4/7/2019"
__python_version__ = "3"



#Double Linked List

class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleList:
    head = None
    tail = None

    def append(self, data): #append new value to the end of the list + add pointer prev pointing to the node before the last
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            #new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        this_node = self.head
        while this_node is not None:
            if this_node.data == node_value:
                if this_node.prev is not None:
                    #re-link pointers to the point we simply "skip" the current node
                    this_node.prev.next = this_node.next
                    this_node.next.prev = this_node.prev
                else:
                    self.head = this_node.next
                    this_node.next.prev = None
            this_node = this_node.next

    def show(self):
        print("FULL Double Linked List:")
        this_node = self.head
        tmp = ""
        while this_node is not None:
            tmp = tmp + str(this_node.data) + " -> "
            this_node = this_node.next
        tmp = tmp + "None"
        print(tmp)


d = DoubleList()

d.append(5)
d.append(8)
d.append(50)

d.show()

d.remove(8)


d.show()