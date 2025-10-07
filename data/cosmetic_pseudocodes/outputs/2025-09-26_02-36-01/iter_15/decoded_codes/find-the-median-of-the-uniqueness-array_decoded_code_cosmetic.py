from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            idx_left = 0
            total_subcount = 0
            element_map = defaultdict(int)
            unique_tracker = 0

            def incrementCount(key):
                nonlocal unique_tracker
                if element_map[key] == 0:
                    unique_tracker += 1
                element_map[key] += 1

            def decrementCount(key):
                nonlocal unique_tracker
                element_map[key] -= 1
                if element_map[key] == 0:
                    unique_tracker -= 1

            def advanceRight(limit):
                nonlocal idx_left
                while limit > idx_left and unique_tracker > target:
                    decrementCount(nums[idx_left])
                    idx_left += 1

            for idx_right in range(len(nums)):
                incrementCount(nums[idx_right])
                advanceRight(idx_right)
                total_subcount += (idx_right - idx_left + 1)

            return total_subcount

        n = len(nums)
        total = n * (n + 1) // 2
        desired_pos = (total + 1) // 2
        lower_bound, upper_bound = 1, n

        while lower_bound < upper_bound:
            median_candidate = (lower_bound + upper_bound) // 2
            if countLessOrEqual(median_candidate) < desired_pos:
                lower_bound = median_candidate + 1
            else:
                upper_bound = median_candidate

        return lower_bound