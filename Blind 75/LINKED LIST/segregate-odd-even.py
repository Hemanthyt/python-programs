class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
     
def segregate(head):  
    os=oe=es=ed=None
    slow=head
    while slow:
        if slow.data % 2 != 0:
            if os is None:
                os=slow
                oe=slow
            else:
                oe.next=slow
                oe=oe.next
        else:
            if es is None:
                es=slow
                ed=slow
            else:
                ed.next=slow
                ed=ed.next
        slow=slow.next
    oe.next=es
    ed.next=None
    return os
def printlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next
        
    
if __name__=="__main__":
    head1=Node(2)
    head1.next=Node(5)
    head1.next.next=Node(3)
    head1.next.next.next=Node(1)
    head1.next.next.next.next=Node(12)
    head=segregate(head1)
    printlist(head)