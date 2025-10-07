from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq_map = Counter(word2)
        window_freq = Counter()
        needed = len(freq_map)
        matched = 0
        start_idx = 0
        total_valid = 0
        idx = 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while idx < len_word1:
            current_char = word1[idx]
            window_freq[current_char] += 1

            if current_char in freq_map and window_freq[current_char] == freq_map[current_char]:
                matched += 1

            while matched == needed and (idx + 1 - start_idx) >= len_word2:
                total_valid += (len_word1 - idx)

                left_char = word1[start_idx]
                window_freq[left_char] -= 1

                if left_char in freq_map and window_freq[left_char] < freq_map[left_char]:
                    matched -= 1

                start_idx += 1

            idx += 1

        return total_valid