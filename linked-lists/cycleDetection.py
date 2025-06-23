class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def cycleDetection(self, head):
        slow, fast  = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper function to create a linked list with cycle
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
    
    # Create the linked list
    head = create_linked_list(arr)
    
    # If pos is -1, no cycle
    if pos == -1:
        return head
    
    # Find the node at position 'pos'
    cycle_start = head
    for i in range(pos):
        if cycle_start:
            cycle_start = cycle_start.next
        else:
            return head  # Invalid position
    
    # Find the last node and connect it to cycle_start
    current = head
    while current.next:
        current = current.next
    current.next = cycle_start
    
    return head

# Test cases
head = create_linked_list_with_cycle([3,2,0,-4], 1)
sol = Solution()
print(sol.cycleDetection(head))



