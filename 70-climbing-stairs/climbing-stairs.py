class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        past = {
            1: 1,
            2: 2
        }

        def helper(n):

            if n not in past:
                past[n] = helper(n - 1) + helper(n - 2)
            
            return past[n]
        
        return helper(n)
        