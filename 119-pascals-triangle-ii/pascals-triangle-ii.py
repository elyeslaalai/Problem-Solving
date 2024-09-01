class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        last = [1, 1]

        for i in range(2, rowIndex + 1):
            temp = [1]
            for j in range(len(last) - 1):
                temp.append(last[j] + last[j + 1])
            temp.append(1)
            last = temp
        
        return last

        