class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        result = []
        first, last = nums[0], nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] - last != 1:
                if first == last:
                    result.append(str(first))
                else:
                    result.append(str(first) + "->" + str(last))
                if i != len(nums):
                    first, last = nums[i], nums[i]
            else:
                last = nums[i]

        return result