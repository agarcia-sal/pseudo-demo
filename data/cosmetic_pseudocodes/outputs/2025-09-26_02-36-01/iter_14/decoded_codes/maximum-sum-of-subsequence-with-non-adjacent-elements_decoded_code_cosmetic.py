class Solution:
    def maximumSumSubsequence(self, nums, queries):
        V_ARBIT = 10**9 + 1
        n = len(nums)
        tmp_a = [0] * n
        tmp_b = [0] * n

        tmp_a[0] = nums[0] if nums[0] > 0 else 0
        tmp_b[0] = 0

        def sub1(i):
            return (0 if tmp_b[i - 1] < 0 else tmp_b[i - 1]) + nums[i]

        def max_of_two(x, y):
            return x if x > y else y

        for i in range(1, n):
            val = sub1(i)
            tmp_a[i] = val if val > 0 else 0
            tmp_b[i] = max_of_two(tmp_b[i - 1], tmp_a[i - 1])

        accum_result = 0
        for p, val in queries:
            nums[p] = val
            if p != 0:
                val_a = tmp_b[p - 1] + nums[p]
                tmp_a[p] = val_a if val_a > 0 else 0
                tmp_b[p] = max_of_two(tmp_b[p - 1], tmp_a[p - 1])
            else:
                tmp_a[p] = nums[p] if nums[p] > 0 else 0
                tmp_b[p] = 0

            idx_update = p + 1
            while idx_update < n:
                val_a = tmp_b[idx_update - 1] + nums[idx_update]
                tmp_a[idx_update] = val_a if val_a > 0 else 0
                tmp_b[idx_update] = max_of_two(tmp_b[idx_update - 1], tmp_a[idx_update - 1])
                idx_update += 1

            accum_result = (accum_result + max_of_two(tmp_a[n - 1], tmp_b[n - 1])) % V_ARBIT

        return accum_result