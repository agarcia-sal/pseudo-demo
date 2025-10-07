from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        total_matches = 0
        frequency_map = defaultdict(int)
        index = len(words) - 1
        while index >= 0:
            current_word = words[index]
            current_len = len(current_word)
            for recorded_key in frequency_map:
                if len(recorded_key) >= current_len:
                    prefix_check = recorded_key.startswith(current_word)
                    suffix_check = recorded_key.endswith(current_word)
                    if prefix_check and suffix_check:
                        total_matches += frequency_map[recorded_key]
            frequency_map[current_word] += 1
            index -= 1
        return total_matches