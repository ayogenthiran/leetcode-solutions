class Solution:
    def reorderList(self, head):
    
        # Step 1: Find the middle of the linked list
        # Use fast/slow pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next        # moves 1 step
            fast = fast.next.next   # moves 2 steps
        
        # Step 2: Reverse the second half
        # Split the list: second half starts from slow.next
        second  = slow.next
        prev = slow.next =  None  # Cut the connection
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Step 3: Merge the two halves
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        return head
    
