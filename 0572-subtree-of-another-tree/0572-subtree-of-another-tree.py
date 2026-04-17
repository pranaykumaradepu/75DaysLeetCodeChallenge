# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        # 1. Base Cases for the search
        # If the subRoot is empty, it's technically a subtree of everything
        if not subRoot:
            return True
        # If the main tree runs out but we are still looking for a subRoot, we failed
        if not root:
            return False
            
        # 2. Check if the trees match perfectly starting at THIS exact node
        if self.isSameTree(root, subRoot):
            return True
            
        # 3. If it didn't match here, keep searching down the left OR right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

   
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)