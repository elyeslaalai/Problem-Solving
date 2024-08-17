class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = len(s) - 1

        while i >= 0 and not s[i].isalnum():
            i -= 1
        
        res = 0
        
        while i >= 0 and s[i] != ' ':
            i -=1
            res +=1 
        

        return res