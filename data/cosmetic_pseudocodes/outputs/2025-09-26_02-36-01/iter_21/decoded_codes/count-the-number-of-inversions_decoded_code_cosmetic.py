class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 7 + (10 ** 9)
        req_dict = {}

        def insertPairs(lst):
            if not lst:
                return
            a, b = lst[0]
            req_dict[a] = b
            insertPairs(lst[1:])

        insertPairs(requirements)

        def count_permutations(aa, bb, cc):
            if aa == n:
                expected_bb = req_dict.get(n, 1) - 1 if n in req_dict else 0
                return 1 if bb == expected_bb else 0

            if aa > 0:
                expected_bb = req_dict.get(aa, bb)
                if bb != expected_bb - 1:
                    return 0

            dd = 0
            for ee in range(n):
                if (cc & (1 << ee)) == 0:
                    ff = bb
                    for gg in range(ee + 1, n):
                        if (cc & (1 << gg)) != 0:
                            ff += 1
                    hh = count_permutations(aa + 1, ff, cc | (1 << ee))
                    dd = (dd + hh) % MOD
            return dd

        return count_permutations(0, 0, 0)