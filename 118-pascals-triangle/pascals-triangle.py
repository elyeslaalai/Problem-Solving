class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]
        
        ans = [[1], [1,1]]
        curr = [1, 1]

        for i in range(3, numRows + 1):

            temp = [1]
            for j in range(len(curr) - 1):
                temp.append(curr[j] + curr[j + 1])
            temp.append(1)
            curr = temp
            ans.append(curr)

        return ans

