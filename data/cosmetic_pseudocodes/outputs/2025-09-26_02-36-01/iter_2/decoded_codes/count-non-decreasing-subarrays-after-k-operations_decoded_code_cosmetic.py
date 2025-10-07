class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        length_of_nums = len(nums)

        def canMakeNonDecreasing(begin, count):
            adjustment_cost = 0
            highest_value = nums[begin]
            index = 1
            while index < count:
                current_value = nums[begin + index]
                if current_value < highest_value:
                    adjustment_cost += highest_value - current_value
                if highest_value < current_value:
                    highest_value = current_value
                if adjustment_cost > k:
                    return False
                index += 1
            return True

        total_possible_subarrays = (length_of_nums * (length_of_nums + 1)) // 2
        count_invalid_subarrays = 0
        start_pos = 0
        while start_pos < length_of_nums:
            lower_bound = 1
            upper_bound = length_of_nums - start_pos
            while lower_bound <= upper_bound:
                midpoint = (lower_bound + upper_bound) // 2
                if canMakeNonDecreasing(start_pos, midpoint):
                    lower_bound = midpoint + 1
                else:
                    upper_bound = midpoint - 1
            count_invalid_subarrays += (length_of_nums - start_pos - upper_bound)
            start_pos += 1

        return total_possible_subarrays - count_invalid_subarrays