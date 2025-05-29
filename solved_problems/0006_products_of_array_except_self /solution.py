from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        res = [0] * n

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] =  nums[i] * prefix[i - 1]

        for i in range(n-2, -1, -1):
            postfix[i] =  nums[i] * postfix[i + 1]

        res[0] = postfix[1]
        res[-1] = prefix[-2]

        for i in range(1, n-1):
            res[i] = prefix[i-1] * postfix[i+1]

        return res
