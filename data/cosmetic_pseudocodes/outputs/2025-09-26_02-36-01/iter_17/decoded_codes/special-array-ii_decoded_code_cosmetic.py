class Solution:
    def isArraySpecial(self, nums, queries):
        alpha = [i % 2 for i in nums]
        beta = [0] * len(nums)
        j = 1
        while j < len(nums):
            if alpha[j] != alpha[j - 1]:
                beta[j] = beta[j - 1]
            else:
                beta[j] = beta[j - 1] + 1
            j += 1

        gamma = []
        for x, y in queries:
            if x == y:
                gamma.append(True)
            else:
                diff = beta[y] - (beta[x] if x > 0 else 0)
                gamma.append(diff == 0)
        return gamma