class Solution:
    def maximumSumSubsequence(self, nums, queries):
        CONST_MOD = 1_000_000_000 + 1
        n = len(nums)
        arr_dp_skip = [0] * n
        arr_dp_take = [0] * n

        arr_dp_take[0] = max(0, nums[0])
        arr_dp_skip[0] = 0

        for idx in range(1, n):
            arr_dp_take[idx] = max(0, arr_dp_skip[idx - 1] + nums[idx])
            arr_dp_skip[idx] = arr_dp_skip[idx - 1] if arr_dp_skip[idx - 1] > arr_dp_take[idx - 1] else arr_dp_take[idx - 1]

        tot_res = 0
        for p, v in queries:
            nums[p] = v
            if p == 0:
                arr_dp_take[0] = max(0, nums[0])
                arr_dp_skip[0] = 0
            else:
                arr_dp_take[p] = max(0, arr_dp_skip[p - 1] + nums[p])
                arr_dp_skip[p] = arr_dp_skip[p - 1] if arr_dp_skip[p - 1] > arr_dp_take[p - 1] else arr_dp_take[p - 1]

            for j in range(p + 1, n):
                arr_dp_take[j] = max(0, arr_dp_skip[j - 1] + nums[j])
                arr_dp_skip[j] = arr_dp_skip[j - 1] if arr_dp_skip[j - 1] > arr_dp_take[j - 1] else arr_dp_take[j - 1]

            max_end = arr_dp_take[-1] if arr_dp_take[-1] > arr_dp_skip[-1] else arr_dp_skip[-1]
            tot_res = (tot_res + max_end) % CONST_MOD

        return tot_res