from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(int)
        for i, value in enumerate(nums):
            indexes[value] = i
        for i, value in enumerate(nums):
            if target - value in indexes and indexes[target - value] != i:
                return [i, indexes[target - value]]
