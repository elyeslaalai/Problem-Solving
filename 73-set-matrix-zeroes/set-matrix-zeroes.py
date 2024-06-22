class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Checks the first row
        for col in range(num_cols):
            if matrix[0][col] == 0:
                first_row_zero = True
                break
        
        # Checks the first col
        for row in range(num_rows):
            if matrix[row][0] == 0:
                first_col_zero = True
                break
        
        # Checks the rest
        for row in range(num_rows):
            for col in range(num_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Replaces the inside
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Replaces the boundaries
        if first_row_zero:
            for col in range(num_cols):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(num_rows):
                matrix[row][0] = 0

        return matrix        
                
        