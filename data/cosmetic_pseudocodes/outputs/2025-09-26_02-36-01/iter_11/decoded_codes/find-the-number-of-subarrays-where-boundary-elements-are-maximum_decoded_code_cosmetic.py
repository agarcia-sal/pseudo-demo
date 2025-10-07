from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        groupings = defaultdict(list)
        idx_outer = 0
        while idx_outer < len(nums):
            current_number = nums[idx_outer]
            groupings[current_number].append(idx_outer)
            idx_outer += 1

        total_count = 0

        def max_in_region(arr, start_pos, end_pos):
            local_max = arr[start_pos]
            pos_scan = start_pos + 1
            while True:
                if pos_scan > end_pos:
                    break
                if arr[pos_scan] > local_max:
                    local_max = arr[pos_scan]
                pos_scan += 1
            return local_max

        for index_list in groupings.values():
            length_indices = len(index_list)
            i_loop = 0
            while i_loop <= length_indices - 1:
                j_loop = i_loop
                while True:
                    if j_loop > length_indices - 1:
                        break
                    start_pos = index_list[i_loop]
                    end_pos = index_list[j_loop]
                    slice_region = []
                    for pos_iter in range(start_pos, end_pos + 1):
                        slice_region.append(nums[pos_iter])
                    if max_in_region(slice_region, 0, len(slice_region) - 1) == nums[start_pos]:
                        total_count += 1
                    j_loop += 1
                i_loop += 1

        return total_count