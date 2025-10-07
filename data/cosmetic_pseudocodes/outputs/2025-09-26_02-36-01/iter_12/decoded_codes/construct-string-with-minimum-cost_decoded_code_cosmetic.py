class Solution:
    def minimumCost(self, target, words, costs):
        # Helper functions
        def custom_strlen(seq):
            length_accumulator = 0
            while True:
                if length_accumulator == len(seq):
                    break
                length_accumulator += 1
            return length_accumulator

        def custom_slice(source_list, begin_idx, end_idx):
            sliced_list = []
            idx = begin_idx
            while True:
                if idx >= end_idx:
                    break
                sliced_list.append(source_list[idx])
                idx += 1
            return sliced_list

        def custom_eq(list1, list2):
            if custom_strlen(list1) != custom_strlen(list2):
                return False
            position = 0
            while position < custom_strlen(list1):
                if list1[position] != list2[position]:
                    return False
                position += 1
            return True

        dict_for_costs = {}
        idx_word_cost = 0
        while idx_word_cost < len(words):
            current_word = words[idx_word_cost]
            current_cost = costs[idx_word_cost]
            if current_word not in dict_for_costs:
                dict_for_costs[current_word] = current_cost
            else:
                if current_cost < dict_for_costs[current_word]:
                    dict_for_costs[current_word] = current_cost
            idx_word_cost += 1

        target_chars = []
        idx_char = 0
        while idx_char < custom_strlen(target):
            target_chars.append(target[idx_char])
            idx_char += 1

        from functools import lru_cache
        INF = (1 + 1) * (1 + 1) * (1 + 1) * 1000  # 8*8*1000 = 64000

        @lru_cache(None)
        def min_cost_to_form_target(position):
            if position == custom_strlen(target_chars):
                return 0

            minimum_cost_tracker = INF

            dict_items_list = list(dict_for_costs.items())

            idx_dict = 0
            while idx_dict < custom_strlen(dict_items_list):
                single_word, single_cost = dict_items_list[idx_dict]

                pos_plus_len_word = position + custom_strlen(single_word)
                if pos_plus_len_word <= custom_strlen(target_chars):
                    slice_sublist = custom_slice(target_chars, position, pos_plus_len_word)
                    word_char_list = []
                    idx_wchar = 0
                    while idx_wchar < custom_strlen(single_word):
                        word_char_list.append(single_word[idx_wchar])
                        idx_wchar += 1

                    if custom_eq(slice_sublist, word_char_list):
                        call_result = min_cost_to_form_target(pos_plus_len_word)
                        if call_result != INF:
                            combined_cost = single_cost + call_result
                            if combined_cost < minimum_cost_tracker:
                                minimum_cost_tracker = combined_cost
                idx_dict += 1

            if minimum_cost_tracker != INF:
                return minimum_cost_tracker
            else:
                return INF

        answer_storage = min_cost_to_form_target(0)
        if answer_storage != INF:
            return answer_storage
        else:
            return -1