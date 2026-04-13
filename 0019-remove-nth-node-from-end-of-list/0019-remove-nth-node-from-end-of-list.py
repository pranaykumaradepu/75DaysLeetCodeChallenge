# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 1. Create a dummy node that points to the head
        dummy = ListNode(0, head)
        
        # 2. Set both pointers. Left starts at dummy, Right starts at head.
        left = dummy
        right = head
        
        # 3. Move the Right pointer 'n' steps ahead to create our "measuring tape" gap
        for _ in range(n):
            right = right.next
            
        # 4. Move both pointers together until Right falls off the end of the list
        while right:
            left = left.next
            right = right.next
            
        # 5. Left is now pointing to the node RIGHT BEFORE the one we want to delete.
        # We simply route its 'next' pointer around the target node.
        left.next = left.next.next
        
        # 6. Return the real head of the list (skipping the dummy)
        return dummy.next