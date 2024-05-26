class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            digits[i], carry =  (digits[i] + carry) % 10, (digits[i] + carry) / 10
            i -= 1
        return [1] + digits if digits[0] == 0 else digits
        