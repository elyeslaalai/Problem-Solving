# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == targetSum
        elif not root.left:
            return self.hasPathSum(root.right, targetSum - root.val)
        elif not root.right:
            return self.hasPathSum(root.left, targetSum - root.val)
        else:
            left_check = self.hasPathSum(root.right, targetSum - root.val)
            right_check = self.hasPathSum(root.left, targetSum - root.val)
            return left_check or right_check
