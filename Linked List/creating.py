class Node:
    def __init__(self,x=None):
        self.data=x
        self.nxt=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print(self):
        temp=self.head
        while (temp):
            print(temp.data,end="-->")
            temp = temp.nxt
# main in first method
lst = linkedlist()
lst.head = Node(30)
e2 = Node(40)
e3 = Node(50)
e4 = Node(60)
lst.head.nxt=e2
e2.nxt=e3
e3.nxt=e4
lst.print()

# main in second method
lst = linkedlist()
e1 = Node(30)
e2 = Node(40)
e3 = Node(50)
e4 = Node(60)
lst.head = e1
e1.nxt=e2
e2.nxt=e3
e3.nxt=e4
lst.print()

output:
   30-->40-->50-->60-->

