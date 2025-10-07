from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(limit):
            tally = defaultdict(int)
            total_subarrays_within_limit = 0
            window_start = 0
            unique_items = 0
            for current_index, current_element in enumerate(nums):
                if tally[current_element] == 0:
                    unique_items += 1
                tally[current_element] += 1
                while unique_items > limit:
                    start_element = nums[window_start]
                    tally[start_element] -= 1
                    if tally[start_element] == 0:
                        unique_items -= 1
                    window_start += 1
                total_subarrays_within_limit += current_index - window_start + 1
            return total_subarrays_within_limit

        length_nums = len(nums)
        total_subarrays = length_nums * (length_nums + 1) // 2
        median_cutoff = (total_subarrays + 1) // 2
        lower_bound = 1
        upper_bound = length_nums

        while lower_bound < upper_bound:
            mid_point = (lower_bound + upper_bound) // 2
            current_count = countLessOrEqual(mid_point)
            if current_count < median_cutoff:
                lower_bound = mid_point + 1
            else:
                upper_bound = mid_point

        return lower_bound