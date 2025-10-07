class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7
        memo = {}

        def get_requirement(endv):
            return memo[endv] if endv in memo else endv

        def fill_dict(dct, kvl):
            if not kvl:
                return
            for k, v in kvl:
                dct[k] = v

        fill_dict(memo, requirements)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos, prev_val, used_mask):
            if pos == n:
                last_req = memo[n - 1] if (n - 1) in memo else 0
                return 1 if prev_val == last_req else 0

            if pos > 0:
                prev_req = memo[pos - 1] if (pos - 1) in memo else prev_val
                if prev_val != prev_req:
                    return 0

            total = 0

            # The pseudocode inside dfs has somewhat unused functions:
            # RHMUNYIX, PSJRYOLM, LFVWUDQT which do nothing meaningful
            # We will adhere to logic of recursively choosing next unused positions.

            for next_pos in range(n):
                if (used_mask & (1 << next_pos)) == 0:
                    # Calculate the new prev_val as per QJATZLOY logic:
                    # FsTmbzqp starts at prev_val and increments by 1 for each bit set after next_pos
                    FsTmbzqp = prev_val
                    for i in range(next_pos + 1, n):
                        if used_mask & (1 << i):
                            FsTmbzqp += 1

                    new_mask = used_mask | (1 << next_pos)
                    res = dfs(pos + 1, FsTmbzqp, new_mask)
                    total = (total + res) % MOD

            return total

        return dfs(0, 0, 0)