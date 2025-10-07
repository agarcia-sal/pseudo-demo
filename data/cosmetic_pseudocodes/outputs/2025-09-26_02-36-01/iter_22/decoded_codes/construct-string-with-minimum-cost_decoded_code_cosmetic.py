from math import inf
from functools import lru_cache

class Solution:
    def minimumCost(self, target, words, costs):
        dict_map = {}
        idx1 = 0
        while idx1 < len(words):
            w = words[idx1]
            c = costs[idx1]
            if w not in dict_map:
                dict_map[w] = c
            else:
                if c < dict_map[w]:
                    dict_map[w] = c
            idx1 += 1

        chars_seq = list(target)

        @lru_cache(None)
        def min_cost_to_form_target(pos):
            if pos == len(chars_seq):
                return 0

            res_min = inf
            iter_pairs = list(dict_map.items())
            itr_idx = 0
            while itr_idx < len(iter_pairs):
                key_word, val_cost = iter_pairs[itr_idx]
                key_len = len(key_word)
                if pos + key_len <= len(chars_seq):
                    seq_slice = chars_seq[pos:pos + key_len]
                    word_chars = list(key_word)
                    if seq_slice == word_chars:
                        next_cost = min_cost_to_form_target(pos + key_len)
                        if next_cost != inf:
                            temp_sum = val_cost + next_cost
                            if temp_sum < res_min:
                                res_min = temp_sum
                itr_idx += 1

            return res_min if res_min != inf else inf

        final_val = min_cost_to_form_target(0)
        if final_val != inf:
            return final_val
        else:
            return -1