class Solution:
    def maximumSumSubsequence(self, nums, queries):
        M = 10**9 + 1
        L = len(nums)
        A = [0] * L
        B = [0] * L

        A[0] = nums[0] if nums[0] > 0 else 0
        B[0] = 0

        for f in range(1, L):
            p = f - 1
            A[f] = max(0, B[p] + nums[f])
            B[f] = max(B[p], A[p])

        R = 0
        for i, v in queries:
            nums[i] = v

            if i == 0:
                A[i] = nums[i] if nums[i] > 0 else 0
                B[i] = 0
            else:
                q = i - 1
                A[i] = max(0, B[q] + nums[i])
                B[i] = max(B[q], A[q])

            j = i + 1
            while j < L:
                k = j - 1
                A[j] = max(0, B[k] + nums[j])
                B[j] = max(B[k], A[k])
                j += 1

            X = max(A[L - 1], B[L - 1])
            R = (R + X) % M

        return R