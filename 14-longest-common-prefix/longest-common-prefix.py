class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = []
        strs = sorted(strs)
        first, last = strs[0], strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ''.join(res)
            else:
                res.append(first[i])
        
        return ''.join(res)

