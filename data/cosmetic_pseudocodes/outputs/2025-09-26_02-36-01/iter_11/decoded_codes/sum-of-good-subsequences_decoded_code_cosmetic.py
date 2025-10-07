from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        constant_val = 10**9 + 7

        delta = defaultdict(int)
        epsilon = defaultdict(int)

        for elem in nums:
            epsilon[elem] = (epsilon[elem] + 1) % constant_val
            delta[elem] = (delta[elem] + elem) % constant_val

            delta[elem] = (delta[elem] + delta[elem - 1] + (epsilon[elem - 1] * elem)) % constant_val
            epsilon[elem] = (epsilon[elem] + epsilon[elem - 1]) % constant_val

            delta[elem] = (delta[elem] + delta[elem + 1] + (epsilon[elem + 1] * elem)) % constant_val
            epsilon[elem] = (epsilon[elem] + epsilon[elem + 1]) % constant_val

        accumulator = 0
        while delta:
            _, val = delta.popitem()
            accumulator = (accumulator + val) % constant_val

        return accumulator