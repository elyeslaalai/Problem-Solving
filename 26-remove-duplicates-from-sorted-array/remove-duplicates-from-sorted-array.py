class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        recent_num = nums[0]
        k = 1

        for i in range(1, len(nums)):
            num = nums[i]
            if num != recent_num:
                recent_num = num
                nums[k] = num
                k += 1
        
        return k
            

