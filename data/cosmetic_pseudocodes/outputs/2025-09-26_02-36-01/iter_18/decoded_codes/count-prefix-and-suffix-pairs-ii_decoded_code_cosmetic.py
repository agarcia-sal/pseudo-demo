from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        tally = 0
        registry = defaultdict(int)

        idx_outer = len(words) - 1
        while idx_outer >= 0:
            current_entry = words[idx_outer]

            for key_iter in registry.keys():
                left_substring = key_iter[:len(current_entry)]
                right_substring = key_iter[-len(current_entry):]

                # Check if current_entry equals both left_substring and right_substring
                if current_entry == left_substring == right_substring:
                    tally += registry[key_iter]

            registry[current_entry] += 1
            idx_outer -= 1

        return tally