class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(thresh):
            def decrement_count(idx, counts_map, unique_c):
                counts_map[nums[idx]] -= 1
                if counts_map[nums[idx]] == 0:
                    unique_c -= 1
                return unique_c

            local_count = 0
            window_start = 0
            occurrences = {}
            unique_elements = 0

            def process_index(r):
                nonlocal local_count, window_start, unique_elements
                if r >= len(nums):
                    return local_count

                if nums[r] not in occurrences or occurrences[nums[r]] == 0:
                    unique_elements += 1
                occurrences[nums[r]] = occurrences.get(nums[r], 0) + 1

                while unique_elements > thresh:
                    unique_elements = decrement_count(window_start, occurrences, unique_elements)
                    window_start += 1

                current_len = r - window_start + 1
                local_count += current_len

                return process_index(r + 1)

            return process_index(0)

        n = len(nums)
        total_subs = n * (n + 1) // 2
        median_idx = (total_subs + 1) // 2

        low_bound, high_bound = 1, n
        while low_bound < high_bound:
            mid_val = (low_bound + high_bound) // 2
            if countLessOrEqual(mid_val) < median_idx:
                low_bound = mid_val + 1
            else:
                high_bound = mid_val

        return low_bound