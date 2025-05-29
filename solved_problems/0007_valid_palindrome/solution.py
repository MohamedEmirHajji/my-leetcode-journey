class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphanumeric = [x.lower() for x in s if x.isalnum()]
        length = len(only_alphanumeric)
        i = 0
        j = length - 1

        while i < j and i < length and j > 0:
            if only_alphanumeric[i] != only_alphanumeric[j]:
                return False
            i += 1
            j -= 1

        return True
