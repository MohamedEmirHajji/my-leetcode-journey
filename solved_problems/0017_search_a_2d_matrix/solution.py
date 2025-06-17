from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        elements_number = len(matrix) * len(matrix[0])
        l, r = 0, elements_number - 1
        cols = len(matrix[0])

        while l <= r:
            i = (l+r) // 2
            row = i // cols
            col = i % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = i - 1
            else:
                l = i + 1

        return False
