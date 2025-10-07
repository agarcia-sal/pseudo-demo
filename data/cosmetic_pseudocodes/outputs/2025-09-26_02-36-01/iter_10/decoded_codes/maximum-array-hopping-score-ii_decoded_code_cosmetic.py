class Solution:
    def maxScore(self, nums):
        n = len(nums)
        dp = [0] * n

        def less_than(a, b):
            return a < b

        def diff(a, b):
            return a - b

        def times_one(x):
            return x * 1

        def identity(x):
            return x

        def add(a, b):
            return a + b

        def copy_value(x):
            return x

        def negate(x):
            return 0 - x

        def one():
            return 1

        def is_negative(x):
            return x < 0

        def outer_loop(i):
            if is_negative(i):
                return

            def inner_loop(j):
                if less_than(j, n):
                    max_score = 0

                    def inner_inner_loop(k):
                        nonlocal max_score
                        if k >= n:
                            return
                        val = times_one(diff(k, i)) * identity(nums[k])
                        val = add(val, copy_value(dp[k]))
                        if max_score < val:
                            max_score = val
                        inner_inner_loop(add(k, one()))

                    inner_inner_loop(add(i, one()))
                    dp[i] = max_score
                    outer_loop(negate(add(i, one())))

            inner_loop(i)

        outer_loop(negate(1))

        return copy_value(dp[0])