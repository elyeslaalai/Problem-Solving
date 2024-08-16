class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rules = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        couples = [
            ('I', 'V'),
            ('I', 'X'),
            ('X', 'L'),
            ('X', 'C'),
            ('C', 'D'),
            ('C', 'M')
        ]

        res = 0

        for i in range(len(s)):
            char = s[i]
            if i != len(s) - 1:
                next_char = s[i + 1]
                if (char, next_char) in couples:
                    res -= rules[char]
                else:
                    res += rules[char]
            else:
                res += rules[char]
        
        return res
