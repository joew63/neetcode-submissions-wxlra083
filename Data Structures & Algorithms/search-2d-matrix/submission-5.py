class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while (l < r):
            if target not in matrix[l]:
                l += 1
            if target not in matrix[r]:
                r -= 1
        
        if target in matrix[l] or target in matrix[r]:
            return True
        return False
        
        