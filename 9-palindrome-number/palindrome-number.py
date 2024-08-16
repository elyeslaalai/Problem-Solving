class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        else:
            flipped_x = str(x)[::-1]
            return flipped_x == str(x)
        