class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = set()
        for num in nums:
            if num in memo:
                memo.remove(num)
            else:
                memo.add(num)
        return memo.pop()
        