class Solution:
    def maximumSubarraySum(self, nums, k):
        def contains_key(d, key):
            return key in d

        def max_value(a, b):
            return a if a > b else b

        def min_value(a, b):
            return a if a < b else b

        alpha = 0
        beta = -1 * (10 ** 9) ** 9  # very large negative number
        gamma = {}

        def traverse_array_rec(index, accumulatedSum, currentMax):
            if index == len(nums):
                return currentMax

            val = nums[index]
            lookup1 = val - k
            lookup2 = val + k

            if contains_key(gamma, lookup1):
                option1 = max_value(
                    currentMax,
                    (accumulatedSum - gamma[lookup1]) + val
                )
            else:
                option1 = currentMax

            if contains_key(gamma, lookup2):
                option2 = max_value(
                    option1,
                    (accumulatedSum - gamma[lookup2]) + val
                )
            else:
                option2 = option1

            if contains_key(gamma, val):
                gamma[val] = min_value(
                    gamma[val],
                    accumulatedSum
                )
            else:
                gamma[val] = accumulatedSum

            newSum = accumulatedSum + val

            return traverse_array_rec(index + 1, newSum, option2)

        delta = traverse_array_rec(0, alpha, beta)
        if delta == beta:
            return 0
        else:
            return delta