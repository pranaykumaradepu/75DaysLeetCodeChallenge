# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

        # If the list is empty or has only one node, it can't have a cycle
        if not head or not head.next:
            return False
            
        # Start both runners at the beginning
        slow = head
        fast = head
        
        # Keep running as long as the fast pointer has a valid path ahead
        while fast and fast.next:
            # Tortoise moves 1 step
            slow = slow.next
            # Hare moves 2 steps
            fast = fast.next.next
            
            # Did they meet?
            if slow == fast:
                return True
                
        # The fast runner hit the end of the list (None)
        return False