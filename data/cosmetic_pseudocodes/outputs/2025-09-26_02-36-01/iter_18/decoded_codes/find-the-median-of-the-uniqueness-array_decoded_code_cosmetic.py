from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def computeCountThreshold(limit):
            accumulator = 0
            start_index = 0
            freq_map = defaultdict(int)
            unique_counter = 0
            current_index = 0
            n = len(nums)

            while current_index < n:
                if freq_map[nums[current_index]] == 0:
                    unique_counter += 1
                freq_map[nums[current_index]] += 1

                while unique_counter > limit:
                    freq_map[nums[start_index]] -= 1
                    if freq_map[nums[start_index]] == 0:
                        unique_counter -= 1
                    start_index += 1

                accumulator += (current_index - start_index) + 1
                current_index += 1

            return accumulator

        length_val = len(nums)
        total_subs = (length_val * (length_val + 1)) // 2
        median_idx = (total_subs + 1) // 2
        lower_bound = 1
        upper_bound = length_val

        def binarySearch():
            nonlocal lower_bound, upper_bound
            while lower_bound < upper_bound:
                mid_point = (lower_bound + upper_bound) // 2
                if computeCountThreshold(mid_point) < median_idx:
                    lower_bound = mid_point + 1
                else:
                    upper_bound = mid_point

        binarySearch()
        return lower_bound