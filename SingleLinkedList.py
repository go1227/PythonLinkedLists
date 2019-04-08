__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "4/7/2019"
__python_version__ = "3"



#Single Linked List

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SingleList:
    head = None
    tail = None

    def append(self, data):  #append new value to the end of the list
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node_value):  #remove the FIRST occurence found of the entered value
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next

    def show(self): #Starting at the head, loop through all nodes (in sequence) and print them out
        print("FULL Single Linked List:")
        current_node = self.head
        tmp = ""
        while current_node is not None:
            tmp = tmp + str(current_node.data) + " -> "
            current_node = current_node.next
        tmp = tmp + "None"
        print(tmp)


sl = SingleList()
sl.append(2)
sl.append(4)
sl.append(6)
sl.append(8)
sl.append(10)
sl.show()

sl.remove(8)
sl.show()

