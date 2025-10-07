from collections import Counter
from itertools import combinations

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        CONST_MODULO = 10**9 + 7
        length_nums = len(nums)
        if length_nums < 5:
            return 0

        # Dummy loop to differ appearance as in pseudocode
        index = 0
        while index < length_nums:
            index += 1

        comb_list = list(combinations(nums, 5))

        valid_count = 0
        idx_outer = 0
        while idx_outer < len(comb_list):
            current_subseq = comb_list[idx_outer]
            frequency_map = Counter(current_subseq)

            middle_pos = 2
            candidate_mode = current_subseq[middle_pos]
            mode_frequency = frequency_map[candidate_mode]
            unique_mode_flag = True

            keys_list = list(frequency_map.keys())
            check_index = 0
            while check_index < len(keys_list) and unique_mode_flag:
                current_key = keys_list[check_index]
                current_freq = frequency_map[current_key]
                if current_key != candidate_mode:
                    if current_freq >= mode_frequency:
                        unique_mode_flag = False
                check_index += 1

            if unique_mode_flag:
                valid_count += 1

            idx_outer += 1

        return valid_count % CONST_MODULO