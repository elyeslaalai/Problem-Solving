class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(needle) > len(haystack):
            return -1
        
        i = 0
        j = len(needle)

        while j <= len(haystack):

            if haystack[i:j] == needle:
                return i
            
            i += 1
            j += 1
        
        return -1