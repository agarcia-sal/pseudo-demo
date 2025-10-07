from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        target_freq = Counter(word2)
        current_freq = Counter()
        total_required = len(target_freq)
        match_count = 0
        start_ptr = 0
        result = 0

        for idx, current_char in enumerate(word1):
            current_freq[current_char] += 1

            if current_char in target_freq and current_freq[current_char] == target_freq[current_char]:
                match_count += 1

            while match_count == total_required and (idx + 1) - start_ptr >= len(word2):
                remaining = len(word1) - idx
                result += remaining

                left_char = word1[start_ptr]
                current_freq[left_char] -= 1

                if left_char in target_freq and current_freq[left_char] < target_freq[left_char]:
                    match_count -= 1

                start_ptr += 1

        return result