class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = []
        shortest_word = strs[0]

        for s in strs:
            if len(s) < len(shortest_word):
                shortest_word = s
        
        for i in range(len(shortest_word)):
            char = shortest_word[i]
            for s in strs:
                if s[i] != char:
                    return ''.join(res)
            res.append(char)
        
        return ''.join(res)

