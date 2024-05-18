class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        
        elif x != 0 and x % 10 == 0:
            return False
        
        else:
            reverse_num = 0
            copy_x = x
            while x != 0:
                reverse_num = reverse_num * 10 + x % 10
                x /= 10
            return reverse_num == copy_x



