class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        recent_num = nums[0]
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != recent_num:
                recent_num = nums[i]
                nums[k] = nums[i]
                k += 1
        
        return k
            

