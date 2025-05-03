class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def checkPalindrome(head):
    slow = head
    stack=[]
    while slow is not None:
        stack.append(slow.data)
        slow=slow.next
    print(stack)
    isPali=True
    slow=head
    while slow is not None:
        if stack.pop()!=slow.data:
            isPali=False
        slow=slow.next
    return isPali

if __name__=="__main__":
    head1=Node(5)
    head1.next=Node(3)
    head1.next.next=Node(3)
    head1.next.next.next=Node(5)
    print(checkPalindrome(head1))  # Output: True