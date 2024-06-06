class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min_str = min(strs)
        max_str = max(strs)
        min_len = min(len(min_str), len(max_str))
        ans = []

        for i in range(min_len):
            if min_str[i] == max_str[i]:
                letter = min_str[i]
                ans.append(letter)
            else:
                return "".join(ans)
        
        return "".join(ans)


