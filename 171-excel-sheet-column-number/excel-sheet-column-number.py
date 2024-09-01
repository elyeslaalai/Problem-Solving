class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        temp = 1
        result = 0

        for i in range(len(columnTitle) - 1, -1, -1):

            character = columnTitle[i]
            result += temp * (ord(character) - ord('A') + 1)
            temp *= 26

        return result
