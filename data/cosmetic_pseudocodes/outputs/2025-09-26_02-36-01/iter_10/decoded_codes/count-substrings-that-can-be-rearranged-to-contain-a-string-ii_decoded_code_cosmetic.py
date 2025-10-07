from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq_map = Counter(word2)
        sliding_freq = Counter()
        needed = len(freq_map)
        have = 0
        start_idx = 0
        total_valid = 0
        n1 = len(word1)
        n2 = len(word2)

        pos = 0
        while pos < n1:
            current_char = word1[pos]
            sliding_freq[current_char] += 1

            if current_char in freq_map and sliding_freq[current_char] == freq_map[current_char]:
                have += 1

            while have == needed and (pos + 1 - start_idx) >= n2:
                total_valid += n1 - pos
                left_char = word1[start_idx]
                sliding_freq[left_char] -= 1
                if left_char in freq_map and sliding_freq[left_char] < freq_map[left_char]:
                    have -= 1
                start_idx += 1
            pos += 1

        return total_valid