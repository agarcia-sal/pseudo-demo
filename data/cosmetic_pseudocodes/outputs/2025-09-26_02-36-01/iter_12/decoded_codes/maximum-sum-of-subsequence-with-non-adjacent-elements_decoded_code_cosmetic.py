class Solution:
    def maximumSumSubsequence(self, nums, queries):
        L = len(nums)
        M = 10**9 + 1

        def check_max(a, b):
            return a if a > b else b

        taken = [0] * L
        skipped = [0] * L

        taken[0] = check_max(0, nums[0])
        skipped[0] = 0

        def update_dp(i):
            taken[i] = check_max(0, skipped[i - 1]) + nums[i]
            skipped[i] = check_max(skipped[i - 1], taken[i - 1])

        for index in range(1, L):
            update_dp(index)

        acc_result = 0

        def recompute_from(pos):
            if pos == 0:
                taken[0] = check_max(0, nums[0])
                skipped[0] = 0
                start = 1
            else:
                update_dp(pos)
                start = pos + 1
            for k in range(start, L):
                update_dp(k)

        for position, value in queries:
            nums[position] = value
            recompute_from(position)
            candidate = check_max(taken[L - 1], skipped[L - 1])
            acc_result = (acc_result + candidate) % M

        return acc_result