class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        length_nums = len(nums)
        length_change = len(changeIndices)

        def can_mark_by_second(limit):
            last_seen = [-1] * length_nums
            pos_counter = 0
            while pos_counter < limit:
                idx_tmp = changeIndices[pos_counter] - 1
                last_seen[idx_tmp] = pos_counter
                pos_counter += 1

            decrements_avail = 0
            marked_set = set()
            idx_loop = 0
            while idx_loop < limit:
                current_idx = changeIndices[idx_loop] - 1
                if current_idx not in marked_set:
                    if last_seen[current_idx] == idx_loop:
                        if nums[current_idx] <= decrements_avail:
                            decrements_avail -= nums[current_idx]
                            marked_set.add(current_idx)
                        else:
                            return False
                    else:
                        decrements_avail += 1
                else:
                    decrements_avail += 1
                idx_loop += 1

            return len(marked_set) == length_nums

        low, high = 0, length_change + 1
        while low < high:
            mid_val = (low + high) // 2
            if can_mark_by_second(mid_val):
                high = mid_val
            else:
                low = low + 1

        return low if low <= length_change else -1