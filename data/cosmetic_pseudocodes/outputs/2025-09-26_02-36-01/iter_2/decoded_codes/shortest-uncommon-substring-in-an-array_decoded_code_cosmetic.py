from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        substr_freq = defaultdict(int)
        for current_str in arr:
            str_len = len(current_str)
            for start_pos in range(str_len):
                for end_pos in range(start_pos + 1, str_len + 1):
                    piece = current_str[start_pos:end_pos]
                    substr_freq[piece] += 1

        results = []
        for string_to_check in arr:
            length_str = len(string_to_check)
            min_unique_substr = ""

            for outer_idx in range(length_str):
                for inner_idx in range(outer_idx + 1, length_str + 1):
                    candidate_substring = string_to_check[outer_idx:inner_idx]
                    if substr_freq[candidate_substring] == 1:
                        if (min_unique_substr == "" or
                            len(candidate_substring) < len(min_unique_substr) or
                            (len(candidate_substring) == len(min_unique_substr) and candidate_substring < min_unique_substr)):
                            min_unique_substr = candidate_substring

            results.append(min_unique_substr)

        return results