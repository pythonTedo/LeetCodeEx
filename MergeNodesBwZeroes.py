from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    head = ListNode(values[0])
    current = head

    for val in range(1, len(values)):
        current.next = ListNode(values[val])
        current = current.next

    return head

linkedList = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])

def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next:
        return None

    ptr = head.next
    sum = 0
    while ptr.val != 0:
        sum += ptr.val
        ptr = ptr.next

    head.next.val = sum
    head.next.next = mergeNodes(ptr)

    return head.next


output = mergeNodes(linkedList)

# Function to print the linked list for verification
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
curr = 0

print_linked_list(output)