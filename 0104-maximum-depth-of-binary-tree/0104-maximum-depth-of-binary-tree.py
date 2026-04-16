# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        # 1. Base Case: If the node is empty, its depth is 0
        if not root:
            return 0
        
        # 2. Ask the left child for its maximum depth
        left_depth = self.maxDepth(root.left)
        
        # 3. Ask the right child for its maximum depth
        right_depth = self.maxDepth(root.right)
        
        # 4. The depth of the current node is the greater of the two depths, 
        # PLUS 1 to count the current node itself.
        return max(left_depth, right_depth) + 1