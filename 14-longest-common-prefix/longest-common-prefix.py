class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strs = sorted(strs)

        if not strs[0]:
            return ""
        
        res = []
        first = strs[0]
        last = strs[-1]
        
        for i in range(len(first)):

            if first[i] == last[i]:
                res.append(first[i])
            
            else:
                return "".join(res)
        
        return "".join(res)


