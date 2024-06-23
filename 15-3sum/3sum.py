class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                num  = nums[i]
                sum  = 0 - num
                low  = i + 1
                high = len(nums) - 1
                
                while low < high:

                    if nums[low] + nums[high] == sum:
                        result.append([num, nums[low], nums[high]])
                        
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        
                        low += 1
                        high -= 1
                        
                    elif nums[low] + nums[high] > sum:
                        high -= 1
                    
                    else:
                        low += 1
        
        return result




            


