class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self, data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return 
        
        current_node=self.head

        while current_node.next is not None:
            current_node=current_node.next
            
        current_node.next=new_node

    def display(self):
        current=self.head
        element=[]
        while current is not None:
            element.append(str(current.data))
            current=current.next
        print("->".join(element)+"-> None")
