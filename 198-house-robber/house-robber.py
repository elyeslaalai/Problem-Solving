class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
        for cur in nums:
            max_3_house_before, max_2_house_before, adjacent = \
            max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
        return max(max_2_house_before, adjacent)
        