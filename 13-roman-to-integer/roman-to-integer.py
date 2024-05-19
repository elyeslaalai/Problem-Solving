class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        for i in range(len(s)):
            char = s[i]
            if (i == len(s) - 1) or (char != 'I' and char != 'X' and char != 'C'):
                res += mapping[char]
            else:
                nextchar = s[i + 1]
                if char == 'I' and (nextchar == 'V' or nextchar == 'X'):
                    res -= mapping[char]
                elif char == 'X' and (nextchar == 'L' or nextchar == 'C'):
                    res -= mapping[char]
                elif char == 'C' and (nextchar == 'D' or nextchar == 'M'):
                    res -= mapping[char]
                else:
                    res += mapping[char]
        
        return res

