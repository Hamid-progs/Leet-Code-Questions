# link: https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in col or i in row:
                    matrix[i][j] = 0
        