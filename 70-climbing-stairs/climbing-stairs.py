class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def climb(n):
            if n == 0 or n == 1:
                return 1
            if n - 1 in memo:
                first_poss = memo[n - 1]
            else:
                first_poss = climb(n - 1)
                memo[n - 1] = first_poss
            if n - 2 in memo:
                second_poss = memo[n - 2]
            else:
                second_poss = climb(n - 2)
                memo[n - 2] = second_poss
            return first_poss + second_poss
        return climb(n)

        