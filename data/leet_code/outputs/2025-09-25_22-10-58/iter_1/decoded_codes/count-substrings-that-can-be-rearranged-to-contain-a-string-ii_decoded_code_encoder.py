from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        word2_count = Counter(word2)
        window_count = Counter()
        required = len(word2_count)
        formed = 0
        left = 0
        valid_substrings = 0

        for right in range(len(word1)):
            char = word1[right]
            window_count[char] += 1

            if char in word2_count and window_count[char] == word2_count[char]:
                formed += 1

            while formed == required and (right + 1 - left) >= len(word2):
                valid_substrings += len(word1) - right
                char_left = word1[left]
                window_count[char_left] -= 1

                if char_left in word2_count and window_count[char_left] < word2_count[char_left]:
                    formed -= 1

                left += 1

        return valid_substrings