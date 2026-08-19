# link: https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix):
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0])
        
        spiral = []

        while top <= bottom and left < right:

            # Traverse top row
            for i in range(left, right):
                spiral.append(matrix[top][i])

            top += 1

            # Traverse right column
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right - 1])

            right -= 1

            # Traverse bottom row
            if top <= bottom:
                for i in range(right - 1, left - 1, -1):
                    spiral.append(matrix[bottom][i])

                bottom -= 1

            # Traverse left column
            if left < right:
                for i in range(bottom, top - 1, -1):
                    spiral.append(matrix[i][left])

                left += 1

        return spiral