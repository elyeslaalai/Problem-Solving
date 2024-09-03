class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        occurences = {}

        for i in range(len(s)):
            occurences[s[i]] = occurences.get(s[i], 0) + 1
            occurences[t[i]] = occurences.get(t[i], 0) - 1
        
        for char in occurences:
            if occurences[char] != 0:
                return False
        
        return True
