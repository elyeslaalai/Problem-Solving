class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n:
            new_n = 0
            while n:
                digit = n % 10
                new_n += digit * digit
                n /= 10
            n = new_n
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        return False

        