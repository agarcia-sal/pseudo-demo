from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        group_store = defaultdict(list)
        ptr_x = 0
        while ptr_x < len(nums):
            val_y = nums[ptr_x]
            group_store[val_y].append(ptr_x)
            ptr_x += 1

        result_accumulator = 0
        value_collections = list(group_store.values())

        idx_p = 0
        while idx_p < len(value_collections):
            subgroup = value_collections[idx_p]
            length_n = len(subgroup)
            i_cursor = 0
            while i_cursor < length_n:
                j_cursor = i_cursor
                while j_cursor < length_n:
                    start_pos = subgroup[i_cursor]
                    end_pos = subgroup[j_cursor]

                    temp_sub = []
                    k_itr = start_pos
                    while k_itr <= end_pos:
                        temp_sub.append(nums[k_itr])
                        k_itr += 1

                    max_val = temp_sub[0]
                    max_ptr = 1
                    while max_ptr < len(temp_sub):
                        if temp_sub[max_ptr] > max_val:
                            max_val = temp_sub[max_ptr]
                        max_ptr += 1

                    reference_val = nums[start_pos]
                    if max_val == reference_val:
                        result_accumulator += 1

                    j_cursor += 1
                i_cursor += 1
            idx_p += 1

        return result_accumulator