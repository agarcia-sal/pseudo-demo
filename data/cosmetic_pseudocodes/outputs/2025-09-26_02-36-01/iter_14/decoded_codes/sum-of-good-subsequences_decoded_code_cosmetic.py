from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        M = 10**9 + 7
        alpha = defaultdict(int)
        beta = defaultdict(int)

        for curr in nums:
            beta[curr] = (beta[curr] + 1) % M
            alpha[curr] = (alpha[curr] + curr) % M

            alpha[curr] = (alpha[curr] + alpha[curr - 1] + beta[curr - 1] * curr) % M
            beta[curr] = (beta[curr] + beta[curr - 1]) % M

            alpha[curr] = (alpha[curr] + alpha[curr + 1] + beta[curr + 1] * curr) % M
            beta[curr] = (beta[curr] + beta[curr + 1]) % M

        aggregate = sum(alpha.values()) % M
        return aggregate