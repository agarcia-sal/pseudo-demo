class Solution:
    def minimumCost(self, target, words, costs):
        def replicate_dictionary(keys_list, values_list):
            def aux(idx, accum_dict):
                if idx == len(keys_list):
                    return accum_dict
                curr_key = keys_list[idx]
                curr_val = values_list[idx]
                if curr_key not in accum_dict:
                    accum_dict[curr_key] = curr_val
                else:
                    if curr_val < accum_dict[curr_key]:
                        accum_dict[curr_key] = curr_val
                return aux(idx + 1, accum_dict)
            return aux(0, {})

        dictionary_word_to_cost = replicate_dictionary(words, costs)
        target_chars = []
        while len(target) != len(target_chars):
            target_chars = target_chars + [target[len(target_chars)]]

        from math import inf
        memo = {}

        def minimum_cost_from_position(position):
            if position == len(target_chars):
                return 0
            if position in memo:
                return memo[position]
            temporary_minimum = inf

            def iterate_dict(pairs, idx):
                nonlocal temporary_minimum
                if idx == len(pairs):
                    return
                word_str, associated_cost = pairs[idx]
                word_len = len(word_str)
                if position + word_len <= len(target_chars):
                    slice_of_target = []
                    for i in range(word_len):
                        slice_of_target = slice_of_target + [target_chars[position + i]]
                    word_as_list = []
                    for j in range(word_len):
                        word_as_list = word_as_list + [word_str[j]]
                    if slice_of_target == word_as_list:
                        next_cost = minimum_cost_from_position(position + word_len)
                        if next_cost != inf and (associated_cost + next_cost) < temporary_minimum:
                            temporary_minimum = associated_cost + next_cost
                iterate_dict(pairs, idx + 1)

            iterate_dict(list(dictionary_word_to_cost.items()), 0)
            memo[position] = temporary_minimum
            return temporary_minimum

        final_answer = minimum_cost_from_position(0)
        if final_answer != inf:
            return final_answer
        return -1