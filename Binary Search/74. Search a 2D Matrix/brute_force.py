from types import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                for item in row:
                    if item == target:
                        return True

        return False
    

# time complexity: O(n^2)
# space complexity: O(1)