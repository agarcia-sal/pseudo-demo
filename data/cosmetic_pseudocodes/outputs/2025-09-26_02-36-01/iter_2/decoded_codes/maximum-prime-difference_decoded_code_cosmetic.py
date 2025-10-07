class Solution:
    def maximumPrimeDifference(self, nums):
        primes_collection = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                             61, 67, 71, 73, 79, 83, 89, 97}
        start_idx = -1
        end_idx = -1
        idx_counter = 0
        while idx_counter < len(nums):
            current_num = nums[idx_counter]
            if current_num in primes_collection:
                if start_idx == -1:
                    start_idx = idx_counter
                end_idx = idx_counter
            idx_counter += 1
        difference = end_idx - start_idx
        return difference