class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: 
        rows = len(matrix)
        cols = len(matrix[0])
        zero_positions = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0: 
                    zero_positions.append((i, j))
        
        for i, j in zero_positions:
            for k in range(cols): 
                matrix[i][k] = 0
            for n in range(rows):
                matrix[n][j] = 0