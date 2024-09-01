class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        result = []

        while columnNumber:
            
            columnNumber -= 1

            offset = columnNumber % 26
            
            result.append(chr(ord('A') + offset))

            columnNumber /= 26
            

        return "".join(result[::-1])