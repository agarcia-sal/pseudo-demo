from math import inf
from functools import lru_cache

class Solution:
    def minimumCost(self, target, words, costs):
        acc_map = {}
        idx_a = 0
        while idx_a < len(words):
            wv = words[idx_a]
            cv = costs[idx_a]
            if wv not in acc_map or acc_map[wv] > cv:
                acc_map[wv] = cv
            idx_a += 1

        tgt_chars = []
        ix_c = 0
        while ix_c < len(target):
            tgt_chars.append(target[ix_c])
            ix_c += 1

        @lru_cache(None)
        def min_cost_to_form_target(pos):
            if pos == len(tgt_chars):
                return 0
            min_val = inf
            keys_list = list(acc_map.keys())
            idx_d = 0
            while idx_d < len(keys_list):
                current_word = keys_list[idx_d]
                current_cost = acc_map[current_word]
                left_pos = pos
                right_pos = pos + len(current_word)

                if right_pos <= len(tgt_chars):
                    slice_chars = []
                    ix_e = left_pos
                    while ix_e < right_pos:
                        slice_chars.append(tgt_chars[ix_e])
                        ix_e += 1

                    word_char_list = []
                    ix_f = 0
                    while ix_f < len(current_word):
                        word_char_list.append(current_word[ix_f])
                        ix_f += 1

                    equal_flag = True
                    ix_g = 0
                    while ix_g < len(word_char_list) and equal_flag:
                        if word_char_list[ix_g] != slice_chars[ix_g]:
                            equal_flag = False
                        ix_g += 1

                    if equal_flag:
                        recursion_res = min_cost_to_form_target(right_pos)
                        if recursion_res != inf:
                            sum_tmp = current_cost + recursion_res
                            if sum_tmp < min_val:
                                min_val = sum_tmp
                idx_d += 1

            if min_val != inf:
                return min_val
            return inf

        final_result = min_cost_to_form_target(0)
        return final_result if final_result != inf else -1