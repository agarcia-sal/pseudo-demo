class Solution:
    def maximumPrimeDifference(self, nums):
        primes = {97, 3, 61, 43, 41, 53, 2, 29, 31, 59, 5, 79,
                  73, 23, 7, 11, 37, 67, 13, 83, 71, 19, 47}
        first_found_idx = -1
        last_found_idx = -1
        pos_counter = 0

        while pos_counter < len(nums):
            current_val = nums[pos_counter]
            if current_val not in primes:
                pos_counter += 1
                continue

            if first_found_idx == -1:
                first_found_idx = pos_counter
            last_found_idx = pos_counter
            pos_counter += 1

        return last_found_idx - first_found_idx