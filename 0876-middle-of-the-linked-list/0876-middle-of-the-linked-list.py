# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Both pointers start at the very beginning
        slow = head
        fast = head
        
        # Keep going as long as the fast pointer can safely take 2 steps
        while fast and fast.next:
            # Slow takes 1 step
            slow = slow.next
            # Fast takes 2 steps
            fast = fast.next.next
            
        # When fast hits the end, slow is perfectly in the middle
        return slow