class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
def reverseLL(head):
    
        
if __name__=="__main__":
    head1=Node(5)
    head1.next=Node(3)
    head1.next.next=Node(3)
    head1.next.next.next=Node(5)
    print(reverseLL(head1))