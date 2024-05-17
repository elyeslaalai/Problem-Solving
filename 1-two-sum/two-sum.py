class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hset = dict()
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num
            if target - num in hset:
                return [i, hset[comp]]
            hset[num] = i