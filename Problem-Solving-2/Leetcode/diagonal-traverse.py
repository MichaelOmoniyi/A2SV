# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rowLen, colLen = len(mat), len(mat[0])
        diagTrav = [0] * (rowLen * colLen)
        count = 0

        row, col = 0, 0

        for _ in range(rowLen * colLen):
            diagTrav[count] = mat[row][col]
            count += 1

            if (row + col) % 2 == 0: # check if the element index is even, for even indexes the traverse direction is usually upward
                if col == (colLen - 1):
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else: # For old indexes the traverse direction is usually downward
                if row == (rowLen - 1):
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1
        return diagTrav