class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) / 2
            middle_element = nums[mid]
            if middle_element == target:
                return mid
            elif middle_element > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

        # 1 3 5 6
        # r, l = 0 [1]
        # 
