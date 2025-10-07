class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        length_nums = len(nums)

        def canMakeNonDecreasing(start_pos, segment_len):
            acc_cost = 0
            max_so_far = nums[start_pos]

            # Recursive helper to check the segment
            def recurseCheck(index):
                nonlocal acc_cost, max_so_far
                if index == segment_len:
                    return True
                current_val = nums[start_pos + index]
                diff = 0
                if current_val < max_so_far:
                    diff = max_so_far - current_val
                acc_cost += diff
                if acc_cost > k:
                    return False
                if max_so_far < current_val:
                    max_so_far = current_val
                return recurseCheck(index + 1)

            return recurseCheck(1)

        total_subarrays = length_nums * (length_nums + 1) // 2
        count_invalid = 0

        def binarySearchCurr(start_index, low_bound, high_bound):
            if low_bound > high_bound:
                return high_bound
            midpoint = (low_bound + high_bound) // 2
            if canMakeNonDecreasing(start_index, midpoint):
                return binarySearchCurr(start_index, midpoint + 1, high_bound)
            else:
                return binarySearchCurr(start_index, low_bound, midpoint - 1)

        for pos in range(length_nums):
            valid_len = binarySearchCurr(pos, 1, length_nums - pos)
            count_invalid += (length_nums - pos) - valid_len

        result = total_subarrays - count_invalid
        return result