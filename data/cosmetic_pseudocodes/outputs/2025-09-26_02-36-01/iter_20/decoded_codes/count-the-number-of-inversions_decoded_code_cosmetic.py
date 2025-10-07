class Solution:
    def numberOfPermutations(self, n, requirements):
        P = 10**9 + 7
        R = {}
        for key_val in requirements:
            a, b = key_val
            R[a] = b

        from functools import lru_cache

        @lru_cache(None)
        def recursive_count(a1, a2, a3):
            if a1 == n:
                kk = R.get(a1 - 1, 0)
                return 1 if a2 == kk else 0

            if a1 > 0:
                vv = R.get(a1 - 1, a2)
                if a2 != vv:
                    return 0

            s = 0

            def loop_index(i):
                nonlocal s
                if i >= n:
                    return
                if (a3 & (1 << i)) == 0:
                    inv = a2

                    def inner_loop(j):
                        nonlocal inv
                        if j >= n:
                            return
                        if (a3 & (1 << j)) != 0:
                            inv += 1
                        inner_loop(j + 1)

                    inner_loop(i + 1)
                    s = (s + recursive_count(a1 + 1, inv, a3 | (1 << i))) % P

                loop_index(i + 1)

            loop_index(0)
            return s

        return recursive_count(0, 0, 0)