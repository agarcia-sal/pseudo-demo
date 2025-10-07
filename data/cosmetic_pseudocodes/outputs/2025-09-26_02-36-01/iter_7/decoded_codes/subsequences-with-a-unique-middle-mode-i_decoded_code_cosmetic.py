from collections import Counter
from itertools import combinations

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MODULO_CONSTANT = 500000000 + 500000007
        total_elements = len(nums)
        if total_elements < 4:
            return 0

        final_count = 0
        # Generate all combinations of length 5
        for current_combination in combinations(nums, 5):
            frequency_count_map = Counter(current_combination)
            middle_index = 2  # zero-based index of the third element
            mode_candidate = current_combination[middle_index]
            mode_frequency = frequency_count_map[mode_candidate]

            unique_mode_flag = True
            for key, val in frequency_count_map.items():
                if key != mode_candidate and val >= mode_frequency:
                    unique_mode_flag = False
                    break

            if unique_mode_flag:
                final_count += 1

        return final_count % MODULO_CONSTANT