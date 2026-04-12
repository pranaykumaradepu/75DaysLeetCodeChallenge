# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
            
        # STEP 1: Find the middle of the list (Tortoise and Hare)
        # We start fast at head.next so 'slow' lands on the exact node we need to split at
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now at the end of the first half. 
        # 'second' is the start of the second half.
        second = slow.next
        slow.next = None # Sever the tie to split the list into two!
        
        # STEP 2: Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 'prev' is now the head of our reversed second half
        second = prev
        first = head
        
        # STEP 3: Merge the two halves alternately
        while second:
            # Save the next nodes before we break the links
            tmp1 = first.next
            tmp2 = second.next
            
            # Zip them together
            first.next = second
            second.next = tmp1
            
            # Move our pointers forward for the next loop
            first = tmp1
            second = tmp2