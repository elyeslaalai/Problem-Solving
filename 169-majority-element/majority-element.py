class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
            if hmap[num] > len(nums) / 2:
                return num
        