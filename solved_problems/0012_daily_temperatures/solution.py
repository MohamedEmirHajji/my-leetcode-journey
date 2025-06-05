from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, x in enumerate(temperatures):
            while stack and x > stack[-1][1]:
                top_element = stack.pop()
                result[top_element[0]] = i - top_element[0]
            stack.append([i, x])
        return result
