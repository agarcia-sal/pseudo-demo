class Solution:
    def subsequencesWithMiddleMode(self, nums):
        mod_value = 10**9 + 7
        length_val = len(nums)

        if length_val < 5:
            return 0

        def get_combinations(arr, r):
            def comb_helper(start_idx, chosen):
                if len(chosen) == r:
                    return [chosen]
                generated = []
                i = start_idx
                while i < len(arr):
                    result_sub = comb_helper(i + 1, chosen + [arr[i]])
                    j = 0
                    while j < len(result_sub):
                        generated.append(result_sub[j])
                        j += 1
                    i += 1
                return generated
            return comb_helper(0, [])

        all_fives = get_combinations(nums, 5)

        final_count = 0
        subseq_idx = 0
        while subseq_idx < len(all_fives):
            curr_subseq = all_fives[subseq_idx]

            def frequency_map(lst):
                freq_dict = {}
                item_idx = 0
                while item_idx < len(lst):
                    current_val = lst[item_idx]
                    freq_dict[current_val] = freq_dict.get(current_val, 0) + 1
                    item_idx += 1
                return freq_dict

            freq_count = frequency_map(curr_subseq)

            mid_idx = 4 - 1  # index 3 (0-based)
            mid_element = curr_subseq[mid_idx]
            mid_element_count = freq_count.get(mid_element, 0)

            unique_mode_flag = True
            key_list = list(freq_count.keys())
            freq_i = 0
            while freq_i < len(key_list):
                element_key = key_list[freq_i]
                element_count = freq_count[element_key]

                if not (element_key != mid_element and element_count >= mid_element_count):
                    freq_i += 1
                    continue
                else:
                    unique_mode_flag = False
                    break

                freq_i += 1

            if unique_mode_flag:
                final_count += 1

            subseq_idx += 1

        return final_count % mod_value