class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]
        
        anagrams = dict()

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s].append(s)
        
        res = []
        for anag in anagrams:
            res.append(anagrams[anag])
        
        return res
        