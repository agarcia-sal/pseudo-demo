class Solution:
    def maxSubstringLength(self, s: str) -> int:
        alpha_freq = {}
        for ch in s:
            alpha_freq[ch] = alpha_freq.get(ch, 0) + 1

        best_len = -1
        n = len(s)
        for outer_idx in range(n):
            segment_freq = {}
            for inner_idx in range(outer_idx, n):
                ch = s[inner_idx]
                segment_freq[ch] = segment_freq.get(ch, 0) + 1

                # Check if segment_freq >= alpha_freq for all chars in segment_freq
                # and the number of distinct chars in segment_freq < distinct chars in alpha_freq
                complete = True
                for k_char in segment_freq:
                    if segment_freq[k_char] < alpha_freq.get(k_char, 0):
                        complete = False
                        break
                if complete and len(segment_freq) < len(alpha_freq):
                    curr_len = inner_idx - outer_idx + 1
                    if best_len < curr_len:
                        best_len = curr_len

        return best_len