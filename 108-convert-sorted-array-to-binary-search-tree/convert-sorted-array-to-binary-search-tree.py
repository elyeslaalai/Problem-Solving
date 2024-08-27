# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        
        def helper(nums, low, high):

            if low > high:
                return None
            
            mid = (low + high) / 2
            root = TreeNode(nums[mid])

            root.left = helper(nums, low, mid - 1)
            root.right = helper(nums, mid + 1, high)

            return root

        
        return helper(nums, 0, len(nums) - 1)
