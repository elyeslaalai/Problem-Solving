class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in num_index:
                return [i, num_index[complement]]
            num_index[num] = i
        
        