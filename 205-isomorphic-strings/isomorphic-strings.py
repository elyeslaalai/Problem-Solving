class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
            
        return True

