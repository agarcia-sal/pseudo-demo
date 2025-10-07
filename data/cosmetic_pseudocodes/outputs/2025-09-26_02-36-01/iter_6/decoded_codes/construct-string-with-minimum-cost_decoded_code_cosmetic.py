class Solution:
    def minimumCost(self, target, words, costs):
        cost_map = {}

        def insert_cost(wd, val):
            if wd not in cost_map:
                cost_map[wd] = val
            else:
                if val < cost_map[wd]:
                    cost_map[wd] = val

        idx1 = 0
        while idx1 < len(words):
            insert_cost(words[idx1], costs[idx1])
            idx1 += 1

        char_list = [c for c in target]
        from math import inf
        memo = {}

        def min_cost_to_form_target(pos):
            if pos == len(char_list):
                return 0
            if pos in memo:
                return memo[pos]

            min_val = inf
            keys_list = list(cost_map.keys())
            rev_keys = []
            idx2 = len(keys_list) - 1
            while idx2 >= 0:
                rev_keys.append(keys_list[idx2])
                idx2 -= 1

            idx3 = 0
            while idx3 < len(rev_keys):
                current_word = rev_keys[idx3]
                current_cost = cost_map[current_word]
                word_len = len(current_word)
                if (pos + word_len) <= len(char_list):
                    segment = []
                    idx4 = pos
                    while idx4 < (pos + word_len):
                        segment.append(char_list[idx4])
                        idx4 += 1
                    word_chars = []
                    idx5 = 0
                    while idx5 < word_len:
                        word_chars.append(current_word[idx5])
                        idx5 += 1
                    equal_check = True
                    idx6 = 0
                    while idx6 < word_len and equal_check:
                        if segment[idx6] != word_chars[idx6]:
                            equal_check = False
                        idx6 += 1
                    if equal_check:
                        rec_res = min_cost_to_form_target(pos + word_len)
                        if rec_res != inf:
                            new_sum = current_cost + rec_res
                            if new_sum < min_val:
                                min_val = new_sum
                idx3 += 1
            if min_val != inf:
                memo[pos] = min_val
                return min_val
            else:
                memo[pos] = inf
                return inf

        answer = min_cost_to_form_target(0)
        if answer != float('inf') and answer != inf:
            return answer
        else:
            return -1