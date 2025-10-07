from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        complete_freq_map = Counter(s)
        answer = -1
        n = len(s)
        for start_idx in range(n):
            partial_freq_map = Counter()
            for end_idx in range(start_idx, n):
                current_char = s[end_idx]
                partial_freq_map[current_char] += 1

                # Check if for all keys in partial_freq_map frequency 
                # is at least complete_freq_map frequency
                all_sufficient = True
                for key in partial_freq_map:
                    if partial_freq_map[key] < complete_freq_map[key]:
                        all_sufficient = False
                        break

                keys_partial = len(partial_freq_map)
                keys_complete = len(complete_freq_map)
                # The substring must have all frequencies at least complete 
                # frequencies but fewer keys (strictly less keys)
                if all_sufficient and keys_partial < keys_complete:
                    current_length = end_idx - start_idx + 1
                    if current_length > answer:
                        answer = current_length
        return answer