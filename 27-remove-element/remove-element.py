class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        k = 0

        for i in range(len(nums)):
            num = nums[i]
            if num != val:
                nums[k] = num
                k += 1
        
        return k

