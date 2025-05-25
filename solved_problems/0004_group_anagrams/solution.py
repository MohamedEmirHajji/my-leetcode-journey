from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        similar_words = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            similar_words[tuple(count)].append(word)
        return list(similar_words.values())
