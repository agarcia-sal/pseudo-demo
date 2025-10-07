from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        def build_map(arr):
            map_dict = defaultdict(list)
            def recurse_enum(pos):
                if pos == len(arr):
                    return
                val = arr[pos]
                map_dict[val].append(pos)
                recurse_enum(pos + 1)
            recurse_enum(0)
            return map_dict

        idx_groups = build_map(nums)
        total_count = 0

        def process_groups(groups_list):
            nonlocal total_count
            if not groups_list:
                return
            curr_indices = groups_list[0]
            len_indices = len(curr_indices)

            def outer_loop(i):
                if i >= len_indices:
                    return
                def inner_loop(j):
                    if j >= len_indices:
                        return
                    start_idx = curr_indices[i]
                    end_idx = curr_indices[j]
                    sub_arr = nums[start_idx:end_idx + 1]

                    max_in_sub = sub_arr[0]
                    def find_max(k):
                        nonlocal max_in_sub
                        if k == len(sub_arr):
                            return max_in_sub
                        if sub_arr[k] > max_in_sub:
                            max_in_sub = sub_arr[k]
                        return find_max(k + 1)
                    max_in_sub = find_max(1)

                    if not (max_in_sub != nums[start_idx]):
                        total_count += 1
                    inner_loop(j + 1)
                inner_loop(i)
                outer_loop(i + 1)

            outer_loop(0)
            process_groups(groups_list[1:])

        process_groups(list(idx_groups.values()))
        final_result = total_count
        return final_result