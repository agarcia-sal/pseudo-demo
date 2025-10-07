from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        total_frequencies = Counter(s)
        longest_substring_length = -1

        n = len(s)
        for start_pos in range(n):
            substring_frequencies = {}
            for end_pos in range(start_pos, n):
                current_char = s[end_pos]
                substring_frequencies[current_char] = substring_frequencies.get(current_char, 0) + 1

                all_chars_satisfied = True
                for char_key in substring_frequencies:
                    if substring_frequencies[char_key] < total_frequencies[char_key]:
                        all_chars_satisfied = False
                        break

                if all_chars_satisfied and len(substring_frequencies) < len(total_frequencies):
                    current_length = end_pos - start_pos + 1
                    if current_length > longest_substring_length:
                        longest_substring_length = current_length

        return longest_substring_length