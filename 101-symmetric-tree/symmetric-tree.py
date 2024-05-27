# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def comparison(p, q):
            if not p and q:
                return False
            elif p and not q:
                return False
            elif not p and not q:
                return True
            else:
                curr_check = p.val == q.val
                next_checks = comparison(p.left, q.right) and comparison(p.right, q.left)
                return curr_check and next_checks
        return comparison(root.left, root.right)