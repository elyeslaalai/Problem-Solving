class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        l, r = 0, x

        while l <= r:
            mid = (l + r) / 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            elif (mid + 1) * (mid + 1) <= x:
                l = mid + 1
        