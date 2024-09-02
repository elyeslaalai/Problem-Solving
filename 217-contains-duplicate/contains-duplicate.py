class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        occurences = set()

        for num in nums:
            if num in occurences:
                return True
            occurences.add(num)
        
        return False
        