class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            copy_x = x
            reverse = 0
            while x != 0:
                reverse = reverse * 10 + x % 10
                x = x / 10
            return reverse == copy_x
