'''
Observations: 
1) Top left is always the smallest element: 
2) bottom right is always the biggest element 
3) Brute force method: check every row and column 

PSDcode: 
row = len(matrix)
col = len(matrix[0])

if target > matrix[row - 1][col - 1] or target < matrix[0][0]: 
    return False

for i in range(row): 
    for j in range(col): 
        if matrix[i][j] == target:
            return True 
        else: 
            return False
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        low, high = 0, row*col - 1

        if target > matrix[row - 1][col - 1] or target < matrix[0][0]: 
            return False
        
        while low <= high: 
            mid = low + ((high - low) // 2)
            if matrix[mid//col][mid%col] < target: 
                low = mid + 1
            elif matrix[mid//col][mid%col] > target: 
                high = mid - 1
            elif matrix[mid//col][mid%col] == target: 
                return True 
            else: 
                pass
        
        return False

        



        