class Solution:
    def minimumDifference(self, nums, k):
        length_of_list = len(nums)
        best_score = float('inf')

        x = 0
        while x <= length_of_list - 1:
            accumulator = 0
            w = x
            while w <= length_of_list - 1:
                accumulator |= nums[w]
                diff_value = abs(k - accumulator)
                if diff_value < best_score:
                    best_score = diff_value
                if best_score == 0:
                    return 0
                w += 1
            x += 1

        return best_score