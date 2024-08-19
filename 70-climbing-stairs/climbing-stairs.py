class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return n
        
        else:

            prev = 1
            curr = 2

            for i in range(3, n + 1):
                temp = curr
                curr += prev
                prev = temp
            
            return curr


            # 1 2 3

        