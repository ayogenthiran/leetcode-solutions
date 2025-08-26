# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

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

# Helper function to convert linked list to Python list for easy printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)
sol = Solution()

print("Original:", linked_list_to_list(head))
reversed_head = sol.reverseList(head)
print("Reversed:", linked_list_to_list(reversed_head))

# Time complexity: O(n)
# Space complexity: O(1)