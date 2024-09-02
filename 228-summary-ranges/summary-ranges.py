class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return ""
        
        if len(nums) == 1:
            num = nums[0]
            print("XXXX")
            return [str(num)]
        
        result = []
        first, last = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num - last == 1:
                last = num
            else:
                if first == last:
                    result.append(str(first))
                else:
                    result.append(str(first) + "->" + str(last))
                first = num
                last = num
        if first == last:
            result.append(str(first))
        else:
            result.append(str(first) + "->" + str(last))
        return result


        