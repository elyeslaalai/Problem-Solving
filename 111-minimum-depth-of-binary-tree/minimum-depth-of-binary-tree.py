# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        elif not root.left and not root.right:
            return 1
        
        elif not root.left and root.right:
            return 1 + self.minDepth(root.right)
        
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        
        else:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))