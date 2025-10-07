from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq_map = Counter(word2)
        window_freq = Counter()
        needed = len(freq_map)
        matched = 0
        start_idx = 0
        substrings_count = 0

        def recursive_slide(right: int, start_idx: int, matched: int, substrings_count: int, window_freq: Counter) -> int:
            if right > len(word1) - 1:
                return substrings_count

            current_char = word1[right]
            window_freq[current_char] = window_freq.get(current_char, 0) + 1

            if current_char in freq_map:
                if window_freq[current_char] == freq_map[current_char]:
                    matched += 1

            while matched == needed and (right + 1 - start_idx) >= len(word2):
                substrings_count += len(word1) - right
                left_char = word1[start_idx]
                window_freq[left_char] -= 1
                if left_char in freq_map and window_freq[left_char] < freq_map[left_char]:
                    matched -= 1
                start_idx += 1

            return recursive_slide(right + 1, start_idx, matched, substrings_count, window_freq)

        total_substrings = recursive_slide(0, start_idx, matched, substrings_count, window_freq)
        return total_substrings