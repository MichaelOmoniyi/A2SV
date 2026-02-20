# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowLen, colLen = len(matrix), len(matrix[0])
        spiralMatrix = []
        directionX, directionY = 1, 0 # Moves right
        row, col = 0, 0

        for _ in range(rowLen * colLen):
            spiralMatrix.append(matrix[row][col])
            matrix[row][col] = "."

            if (0 <= row + directionY < rowLen and 0 <= col + directionX < colLen and matrix[row + directionY][col + directionX] != "."):
                row, col = row + directionY, col + directionX
            else:
                directionX, directionY = -directionY, directionX # Turns 90deg
                row, col = row + directionY, col + directionX
        return spiralMatrix