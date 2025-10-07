class Solution:
    def earliestSecondToMarkIndices(self, changeIndices: list[int], nums: list[int]) -> int:
        def helper_can_mark_by_second(x: int) -> bool:
            marker_times = [-1] * len(nums)
            idx_counter = 0
            while idx_counter < x:
                cur_idx = changeIndices[idx_counter] - 1
                marker_times[cur_idx] = idx_counter
                idx_counter += 1

            total_needed = sum(nums)

            decrements_available = 0
            marked_set = set()

            scan_pos = 0
            while scan_pos < x:
                current_pos = changeIndices[scan_pos] - 1
                if current_pos not in marked_set:
                    if marker_times[current_pos] == scan_pos:
                        if nums[current_pos] <= decrements_available:
                            decrements_available -= nums[current_pos]
                            marked_set.add(current_pos)
                        else:
                            return False
                    else:
                        decrements_available += 1
                else:
                    decrements_available += 1
                scan_pos += 1

            return len(marked_set) == len(nums)

        low_bound = 0
        high_bound = len(changeIndices) + 1

        while low_bound < high_bound:
            midpoint = (low_bound + high_bound) // 2
            if helper_can_mark_by_second(midpoint):
                high_bound = midpoint
            else:
                low_bound += 1

        if low_bound <= len(changeIndices):
            return low_bound
        else:
            return -1