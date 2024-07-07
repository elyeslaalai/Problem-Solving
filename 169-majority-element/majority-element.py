class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_element = nums[0]
        maj_occurences = 1

        for i in range(1, len(nums)):

            num = nums[i]

            if num == maj_element:
                maj_occurences += 1
            
            else:
                maj_occurences -= 1
                
                if maj_occurences == 0:
                    maj_occurences = 1
                    maj_element = num

        return maj_element