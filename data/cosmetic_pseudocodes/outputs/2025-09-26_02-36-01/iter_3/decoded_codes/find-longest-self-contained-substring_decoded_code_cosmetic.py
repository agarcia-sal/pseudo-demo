from collections import Counter

class Solution:
    def maxSubstringLength(self, s):
        total_freq = Counter()
        pos = 0
        n = len(s)
        while pos < n:
            ch = s[pos]
            total_freq[ch] += 1
            pos += 1

        result_length = -1
        start_idx = 0
        total_keys = set(total_freq.keys())
        while start_idx < n:
            substring_freq = Counter()
            end_idx = start_idx
            while end_idx < n:
                current_char = s[end_idx]
                substring_freq[current_char] += 1

                # Check if for all keys in substring_freq freq >= total_freq
                valid_subset = True
                for key_ch in substring_freq:
                    if substring_freq[key_ch] < total_freq[key_ch]:
                        valid_subset = False
                        break

                if valid_subset and (len(substring_freq) < len(total_keys)):
                    sub_len = end_idx - start_idx + 1
                    if sub_len > result_length:
                        result_length = sub_len
                end_idx += 1
            start_idx += 1

        return result_length