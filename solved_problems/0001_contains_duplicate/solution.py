from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for x in nums:
            if count[x] == 1:
                return True
            else:
                count[x] += 1
        return False
