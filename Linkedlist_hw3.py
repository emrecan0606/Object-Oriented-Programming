# Double linked list Homework
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList: 
    def __init__(self): 
        self.head = None

    def append(self, data): 
        if self.head is None: 
            new_node = Node(data) 
            new_node.prev = None 
            self.head = new_node 
        else:
            new_node = Node(data) 
            cur = self.head 
            while cur.next: 
                cur = cur.next 
            cur.next = new_node
            new_node.prev = cur 
            new_node.next = None 

    def prepend(self, data): 
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None 
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node 
            new_node.next = self.head 
            self.head = new_node
            new_node.prev = None 
        

    def print_list(self): 
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dobllist = DoublyLinkedList()
dobllist.prepend(0)
dobllist.append(1)
dobllist.append(2)
dobllist.append(3)
dobllist.append(4)
dobllist.prepend(5)

dobllist.print_list()