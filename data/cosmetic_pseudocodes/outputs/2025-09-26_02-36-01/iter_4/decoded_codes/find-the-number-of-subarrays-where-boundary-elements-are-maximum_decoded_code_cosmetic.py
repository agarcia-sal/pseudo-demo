from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        index_map = defaultdict(list)

        for pos_counter, current_number in enumerate(nums):
            index_map[current_number].append(pos_counter)

        total_count = 0
        for indices_list in index_map.values():
            list_length = len(indices_list)
            for outer_idx in range(list_length):
                for inner_idx in range(outer_idx, list_length):
                    start_pos = indices_list[outer_idx]
                    end_pos = indices_list[inner_idx]
                    subarray_slice = nums[start_pos:end_pos+1]

                    highest_value = subarray_slice[0]
                    for element in subarray_slice:
                        if element > highest_value:
                            highest_value = element

                    if highest_value == nums[start_pos]:
                        total_count += 1

        return total_count