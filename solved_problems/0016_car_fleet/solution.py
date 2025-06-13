from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[x, y] for x, y in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for x, y in pairs:
            stack.append((target - x) / y)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
