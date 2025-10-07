class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        def evaluateFeasibility(origin, span):
            expense = 0
            threshold = nums[origin]

            def maximum(a, b):
                return a if a > b else b

            index = 1
            while index < span:
                if nums[origin + index] < threshold:
                    expense += threshold - nums[origin + index]
                threshold = maximum(threshold, nums[origin + index])
                if expense > k:
                    return False
                index += 1
            return True

        length = len(nums)
        all_subs = length * (length + 1) // 2
        rejected = 0

        base = 0
        while base < length:
            minimal, maximal = 1, length - base
            while minimal <= maximal:
                midpoint = (minimal + maximal) // 2
                if evaluateFeasibility(base, midpoint):
                    minimal = midpoint + 1
                else:
                    maximal = midpoint - 1
            rejected += (length - base - maximal)
            base += 1

        return all_subs - rejected