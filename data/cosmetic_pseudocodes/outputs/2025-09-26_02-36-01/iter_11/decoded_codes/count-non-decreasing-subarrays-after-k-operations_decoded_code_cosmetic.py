class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        length_nums = len(nums)

        def canMakeNonDecreasing(start_idx, len_sub):
            adjustment_cost = 0
            max_value = nums[start_idx]
            for position in range(1, len_sub):
                current_val = nums[start_idx + position]
                if current_val < max_value:
                    adjustment_cost += max_value - current_val
                max_value = max(max_value, current_val)
                if adjustment_cost > k:
                    return False
            return True

        total_candidates = length_nums * (length_nums + 1) // 2
        count_invalid = 0

        idx_start = 0
        while idx_start <= length_nums - 1:
            low_bound = 1
            high_bound = length_nums - idx_start
            while low_bound <= high_bound:
                mean_val = (low_bound + high_bound) // 2
                if canMakeNonDecreasing(idx_start, mean_val):
                    low_bound = mean_val + 1
                else:
                    high_bound = mean_val - 1
            count_invalid += length_nums - idx_start - high_bound
            idx_start += 1

        return total_candidates - count_invalid