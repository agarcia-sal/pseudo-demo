class Solution:
    def countOfPairs(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        max_val = float('-inf')

        def find_max(lst, idx, acc):
            if idx < 0:
                return acc
            else:
                if lst[idx] > acc:
                    return find_max(lst, idx - 1, lst[idx])
                else:
                    return find_max(lst, idx - 1, acc)

        max_val = find_max(nums, n - 1, max_val)

        def zero_1d_array(z):
            if z == 0:
                return []
            return [0] + zero_1d_array(z - 1)

        def zero_2d_array(y, z):
            if y == 0:
                return []
            head = zero_1d_array(z)
            tail = zero_2d_array(y - 1, z)
            return [head] + tail

        def zero_3d_array(x, y, z):
            if x == 0:
                return []
            head = zero_2d_array(y, z)
            tail = zero_3d_array(x - 1, y, z)
            return [head] + tail

        dp = zero_3d_array(n + 1, max_val + 1, max_val + 1)

        first_num = nums[0]
        w = 0
        while w <= first_num:
            dp[1][w][first_num - w] = 1
            w += 1

        def loop_i(i):
            if i > n:
                return

            pj = 0

            def loop_j():
                nonlocal pj
                if pj > nums[i - 1]:
                    return

                pk = 0

                def loop_k():
                    nonlocal pk
                    if pk > nums[i - 1]:
                        return

                    if pj + pk == nums[i - 1]:
                        prev_j = 0

                        def loop_prev_j():
                            nonlocal prev_j
                            if prev_j > pj:
                                return

                            prev_k = pk

                            def loop_prev_k():
                                nonlocal prev_k
                                if prev_k > max_val:
                                    return

                                dp[i][pj][pk] += dp[i - 1][prev_j][prev_k]
                                if dp[i][pj][pk] >= MOD:
                                    dp[i][pj][pk] -= MOD

                                prev_k += 1
                                loop_prev_k()

                            loop_prev_k()

                            prev_j += 1
                            loop_prev_j()

                        loop_prev_j()

                    pk += 1
                    loop_k()

                loop_k()

                pj += 1
                loop_j()

            loop_j()

            loop_i(i + 1)

        loop_i(2)

        res = 0
        z = 0
        while z <= max_val:
            l = 0
            while l <= max_val:
                res += dp[n][z][l]
                if res >= MOD:
                    res -= MOD
                l += 1
            z += 1

        return res