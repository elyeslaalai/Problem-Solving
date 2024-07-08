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
        if not root:
            return True
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        if not root:
            return True
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        root_is_balanced = abs(left_depth - right_depth) <= 1
        left_is_balanced = self.isBalanced(root.left)
        right_is_balanced = self.isBalanced(root.right)
        return root_is_balanced and left_is_balanced and right_is_balanced
