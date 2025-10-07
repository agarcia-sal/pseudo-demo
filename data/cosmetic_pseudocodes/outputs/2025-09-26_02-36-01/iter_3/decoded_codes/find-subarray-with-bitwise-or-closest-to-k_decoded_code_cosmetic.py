class Solution:
    def minimumDifference(self, nums, k):
        count = len(nums)
        minimum_gap = 10**9 + 7  # Large number representing infinity

        left = 0
        while left < count:
            aggregate_or = 0
            right = left
            while right < count:
                aggregate_or |= nums[right]
                difference = abs(k - aggregate_or)
                if difference < minimum_gap:
                    minimum_gap = difference
                if minimum_gap == 0:
                    return 0
                right += 1
            left += 1
        return minimum_gap