class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
            
        ROWS = len(matrix)
        COLS = len(matrix[0])
    
        left = 0
        right = (ROWS * COLS) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            row = mid // COLS
            col = mid % COLS
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False