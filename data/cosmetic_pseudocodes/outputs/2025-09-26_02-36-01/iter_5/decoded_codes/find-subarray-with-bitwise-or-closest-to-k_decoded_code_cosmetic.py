class Solution:
    def minimumDifference(self, nums, k):
        length_nums = len(nums)
        best_diff = (1 << 31) * 2  # large number instead of infinity

        start_index = 0
        while start_index < length_nums:
            aggregate_or = 0
            end_index = start_index
            while end_index < length_nums:
                aggregate_or |= nums[end_index]
                difference = k - aggregate_or
                if difference < 0:
                    difference = -difference

                if difference < best_diff:
                    best_diff = difference

                if best_diff == 0:
                    return 0

                end_index += 1
            start_index += 1

        return best_diff