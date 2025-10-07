class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        length_of_nums = len(nums)

        def canMakeNonDecreasing(start_segment, segment_len):
            penalty = 0
            highest_value = nums[start_segment]
            index_counter = 1

            while index_counter < segment_len:
                current_element = nums[start_segment + index_counter]
                if current_element < highest_value:
                    penalty += highest_value - current_element
                if highest_value < current_element:
                    highest_value = current_element
                if penalty > k:
                    return False
                index_counter += 1

            return True

        total_possible_subarrays = length_of_nums * (length_of_nums + 1) // 2
        count_invalid_subarrays = 0

        main_index = 0
        while main_index < length_of_nums:
            lower_bound = 1
            upper_bound = length_of_nums - main_index

            while lower_bound <= upper_bound:
                midpoint = (lower_bound + upper_bound) // 2
                if canMakeNonDecreasing(main_index, midpoint):
                    lower_bound = midpoint + 1
                else:
                    upper_bound = midpoint - 1

            count_invalid_subarrays += length_of_nums - main_index - upper_bound
            main_index += 1

        return total_possible_subarrays - count_invalid_subarrays