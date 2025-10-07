class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        total_length = len(nums)

        def canMakeNonDecreasing(position, count):
            adjustment = 0
            highest_val = nums[position]
            index = 1
            while index < count:
                if nums[position + index] < highest_val:
                    adjustment += highest_val - nums[position + index]
                else:
                    highest_val = nums[position + index]
                if adjustment > k:
                    return False
                index += 1
            return True

        max_possible_subarrays = total_length * (total_length + 1) // 2
        count_invalid = 0

        outer_ptr = 0
        while outer_ptr < total_length:
            min_bound = 1
            max_bound = total_length - outer_ptr
            valid_len = 0
            while min_bound <= max_bound:
                mid_val = (min_bound + max_bound) // 2
                if canMakeNonDecreasing(outer_ptr, mid_val):
                    valid_len = mid_val
                    min_bound = mid_val + 1
                else:
                    max_bound = mid_val - 1
            count_invalid += (total_length - outer_ptr - valid_len)
            outer_ptr += 1

        return max_possible_subarrays - count_invalid