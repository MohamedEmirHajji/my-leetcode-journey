from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                current_length = 1
                while n + current_length in nums_set:
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length
