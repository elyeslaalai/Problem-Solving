# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(root):
            if not root:
                return 0
            if not root.left:
                return 1 + depth(root.right)
            if not root.right:
                return 1 + depth(root.left)
            return 1 + max(depth(root.left), depth(root.right))
        
        if not root:
            return True
        
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

