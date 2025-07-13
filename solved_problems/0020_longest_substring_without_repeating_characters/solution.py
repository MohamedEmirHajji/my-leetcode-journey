class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        j = 0
        result = 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[j])
                j += 1
            visited.add(s[i])
            result = max(result, i - j + 1)

        return result
