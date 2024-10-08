# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def dfs(root, result):
            if not root:
                return
            result.append(root.val)
            dfs(root.left, result)
            dfs(root.right, result)
            return result
        return dfs(root, result)