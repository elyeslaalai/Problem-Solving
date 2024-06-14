class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        hset_rows = set()
        hset_cols = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    hset_rows.add(r)
                    hset_cols.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in hset_rows or c in hset_cols:
                    matrix[r][c] = 0
        return matrix


        