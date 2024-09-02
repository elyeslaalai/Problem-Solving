class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        occurences = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in occurences and abs(occurences[num] - i) <= k:
                return True
            occurences[num] = i
        
        return False
        