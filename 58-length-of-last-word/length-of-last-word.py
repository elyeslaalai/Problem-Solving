class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        ans = 0
        while i >= 0 and s[i] != ' ':
            ans += 1
            i -= 1
        return ans