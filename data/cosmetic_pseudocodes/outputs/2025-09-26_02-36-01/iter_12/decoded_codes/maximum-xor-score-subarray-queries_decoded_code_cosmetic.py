class Solution:
    def maximumSubarrayXor(self, nums, queries):
        n = len(nums)

        def xor_compute(x, y):
            return x ^ y

        def maximum(x, y, z):
            if x >= y:
                if x >= z:
                    return x
                else:
                    return z
            else:
                if y >= z:
                    return y
                else:
                    return z

        def fill_matrix(size):
            return [[0] * size for _ in range(size)]

        f = fill_matrix(n)
        g = fill_matrix(n)

        def loop_i(index):
            if index < 0:
                return
            f[index][index] = nums[index]
            g[index][index] = nums[index]

            def loop_j(jindex):
                if jindex > n - 1:
                    return
                f[index][jindex] = xor_compute(f[index][jindex - 1], f[index + 1][jindex])
                g[index][jindex] = maximum(g[index][jindex], g[index][jindex - 1], g[index + 1][jindex])
                loop_j(jindex + 1)

            loop_j(index + 1)
            loop_i(index - 1)

        loop_i(n - 1)

        result = []

        def collect_query(idx):
            if idx >= len(queries):
                return
            l, r = queries[idx]
            result.append(g[l][r])
            collect_query(idx + 1)

        collect_query(0)
        return result