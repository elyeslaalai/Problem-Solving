class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        possible_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        possible_strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = []
        i = 0 

        while num:
            while num >= possible_nums[i]:
                ans.append(possible_strs[i])
                num -= possible_nums[i]
            i += 1
        
        return "".join(ans)
                

        