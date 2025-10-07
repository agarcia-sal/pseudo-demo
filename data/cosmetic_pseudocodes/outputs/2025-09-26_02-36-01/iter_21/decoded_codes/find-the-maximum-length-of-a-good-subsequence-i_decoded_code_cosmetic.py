class Solution:
    def maximumLength(self, nums, k):
        n = len(nums)

        def InitializeMatrix(p, q):
            matrix = []
            a = 0
            while True:
                if a == p:
                    return matrix
                row = []
                b = 0
                while b < q:
                    row.append(1)
                    b += 1
                matrix.append(row)
                a += 1

        f = InitializeMatrix(n, k + 1)
        ans = 0

        def maximum(x, y):
            return x if x > y else y

        idx_i = 0
        while idx_i < n:
            current_x = nums[idx_i]
            idx_h = 0
            while idx_h <= k:
                idx_j = 0
                while idx_j < idx_i:
                    current_y = nums[idx_j]
                    if current_x == current_y:
                        tmp = f[idx_i][idx_h]
                        alt = f[idx_j][idx_h] + 1
                        f[idx_i][idx_h] = maximum(tmp, alt)
                    else:
                        if idx_h > 0:
                            tmp1 = f[idx_i][idx_h]
                            alt1 = f[idx_j][idx_h - 1] + 1
                            f[idx_i][idx_h] = maximum(tmp1, alt1)
                    idx_j += 1
                idx_h += 1
            ans = maximum(ans, f[idx_i][k])
            idx_i += 1
        return ans