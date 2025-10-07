from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        QUAZ = 10**9 + 7
        f_map = defaultdict(int)
        g_map = defaultdict(int)

        a1 = 0
        while a1 < len(nums):
            b2 = nums[a1]

            t5 = g_map[b2]
            t6 = f_map[b2]

            g_map[b2] = (t5 + 1) % QUAZ
            f_map[b2] = (t6 + b2) % QUAZ

            p1 = f_map[b2 - 1]
            q1 = g_map[b2 - 1]

            s1 = (p1 + q1 * b2) % QUAZ
            f_map[b2] = (f_map[b2] + s1) % QUAZ
            g_map[b2] = (g_map[b2] + q1) % QUAZ

            p2 = f_map[b2 + 1]
            q2 = g_map[b2 + 1]

            s2 = (p2 + q2 * b2) % QUAZ
            f_map[b2] = (f_map[b2] + s2) % QUAZ
            g_map[b2] = (g_map[b2] + q2) % QUAZ

            a1 += 1

        accumulator = 0
        for key in f_map:
            accumulator += f_map[key]

        return accumulator % QUAZ