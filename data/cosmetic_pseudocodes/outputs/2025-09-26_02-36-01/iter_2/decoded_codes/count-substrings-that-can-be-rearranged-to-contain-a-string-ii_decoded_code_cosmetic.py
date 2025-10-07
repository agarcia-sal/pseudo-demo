from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq_word2 = Counter(word2)
        freq_window = Counter()
        needed_types = len(freq_word2)
        matched_types = 0
        start_index = 0
        total_valid = 0

        for idx, current_char in enumerate(word1):
            freq_window[current_char] += 1

            if current_char in freq_word2 and freq_window[current_char] == freq_word2[current_char]:
                matched_types += 1

            while matched_types == needed_types and (idx + 1 - start_index) >= len(word2):
                total_valid += len(word1) - idx

                left_char = word1[start_index]
                freq_window[left_char] -= 1

                if left_char in freq_word2 and freq_window[left_char] < freq_word2[left_char]:
                    matched_types -= 1

                start_index += 1

        return total_valid