class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        result = []

        while columnNumber:
            
            offset = (columnNumber - 1) % 26
            
            result.append(chr(ord('A') + offset))

            columnNumber = (columnNumber - 1) / 26
            

        return "".join(result[::-1])