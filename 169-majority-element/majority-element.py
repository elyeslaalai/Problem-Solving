class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maj, occ = nums[0], 1

        for i in range(1, len(nums)):
            num = nums[i]
            if num == maj:
                occ += 1
            else:
                occ -= 1
                if occ < 0:
                    maj = num
                    occ = 1
        
        return maj
            



        