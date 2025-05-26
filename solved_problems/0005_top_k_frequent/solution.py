from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        group_dict = defaultdict(list)
        result = []

        for n in nums:
            count_dict[n] += 1

        for key, value in count_dict.items():
            group_dict[value].append(key)

        top_k_count = sorted(group_dict.keys(), reverse=True)[:k]

        for i in top_k_count:
            for j in group_dict[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result
