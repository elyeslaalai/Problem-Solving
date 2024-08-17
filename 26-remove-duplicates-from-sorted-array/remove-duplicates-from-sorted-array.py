class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 1

        temp = nums[0]

        for j in range(1, len(nums)):

            num = nums[j]

            if num != temp:

                nums[i] = num
                temp = num
                i += 1
        
        return i


        