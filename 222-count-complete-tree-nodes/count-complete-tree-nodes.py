import math
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leftHeight(root):
            if not root:
                return 0
            return 1 + leftHeight(root.left)
        def rightHeight(root):
            if not root:
                return 0
            return 1 + rightHeight(root.right)
        if not root:
            return 0
        leftHeight = leftHeight(root)
        rightHeight = rightHeight(root)
        if leftHeight == rightHeight:
            return int(math.pow(2, leftHeight)) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1