class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self, data=None):
        self.head=data	
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


daysofweek = LinkedList()
daysofweek.append('‘Tues’, ‘Wed’, ‘Fri')



