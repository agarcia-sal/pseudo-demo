from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        count_word2 = Counter(word2)
        window = Counter()
        needed = len(count_word2)
        formed = 0
        start = 0
        total_valid = 0

        for end, current_char in enumerate(word1):
            window[current_char] += 1

            if current_char in count_word2 and window[current_char] == count_word2[current_char]:
                formed += 1

            while formed == needed and (end - start + 1) >= len(word2):
                total_valid += len(word1) - end
                left_char = word1[start]
                window[left_char] -= 1

                if left_char in count_word2 and window[left_char] < count_word2[left_char]:
                    formed -= 1

                start += 1

        return total_valid