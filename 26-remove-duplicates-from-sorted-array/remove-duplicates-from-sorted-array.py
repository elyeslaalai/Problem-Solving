class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        hset = set()
        for i in range(len(nums)):
            num = nums[i]
            if num not in hset:
                hset.add(num)
                nums[k] = num
                k += 1
        return k
