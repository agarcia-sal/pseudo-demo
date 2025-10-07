class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            tally = 0
            start_idx = 0
            freq_map = {}
            unique_elements = 0
            for end_idx, val in enumerate(nums):
                if freq_map.get(val, 0) == 0:
                    unique_elements += 1
                freq_map[val] = freq_map.get(val, 0) + 1
                while unique_elements > target:
                    freq_map[nums[start_idx]] -= 1
                    if freq_map[nums[start_idx]] == 0:
                        unique_elements -= 1
                    start_idx += 1
                tally += (end_idx - start_idx + 1)
            return tally

        n = len(nums)
        total_count = n * (n + 1) // 2
        target_pos = (total_count + 1) // 2
        min_value, max_value = 1, n
        while min_value != max_value:
            midpoint = (min_value + max_value) // 2
            if countLessOrEqual(midpoint) < target_pos:
                min_value = midpoint + 1
            else:
                max_value = midpoint
        return min_value