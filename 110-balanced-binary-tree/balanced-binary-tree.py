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
            elif not root.left and not root.right:
                return 1
            elif not root.left:
                return 1 + depth(root.right)
            elif not root.right:
                return 1 + depth(root.left)
            else:
                return 1 + max(depth(root.right), depth(root.left))
        if not root:
            return True
        left_depth = 0 if not root.left else depth(root.left)
        right_depth = 0 if not root.right else depth(root.right)
        curr_check = abs(left_depth - right_depth) <= 1
        left_check = self.isBalanced(root.left)
        right_check = self.isBalanced(root.right)
        return curr_check and left_check and right_check
            

