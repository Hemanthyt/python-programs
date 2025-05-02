class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
def mergeLL(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <=head2.data:
        head1.next=mergeLL(head1.next,head2)
        return head1
    else:
        head2.next=mergeLL(head1,head2.next)
        return head2
def printlist(head):
    curr=head
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next

if __name__=="__main__":
    head1=Node(5)
    head1.next=Node(10)
    head1.next.next=Node(15)
    head2=Node(2)
    head2.next=Node(3)
    head2.next.next=Node(20)
    head= mergeLL(head1,head2)
    printlist(head)