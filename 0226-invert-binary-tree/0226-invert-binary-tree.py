# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        # 1. Base Case: If the node is empty, stop and return None
        if not root:
            return None
            
        # 2. The Swap: Swap the left and right children
        # Python allows us to do this cleanly in one line
        root.left, root.right = root.right, root.left
        
        # 3. The Delegation: Recursively call the function on the new children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 4. Return the root node of the newly inverted (sub)tree
        return root