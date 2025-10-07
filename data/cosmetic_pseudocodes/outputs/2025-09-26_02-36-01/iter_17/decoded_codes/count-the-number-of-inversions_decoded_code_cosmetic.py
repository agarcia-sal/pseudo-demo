class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        M = 10**9 + 7
        mapReq = {}
        p = 0
        while p < len(requirements):
            k, v = requirements[p]
            mapReq[k] = v
            p += 1

        def count_permutations(L: int, inv: int, used: int) -> int:
            if L == n:
                target = mapReq.get(n - 1, 0)
                return 1 if inv == target else 0

            if L > 0:
                expected = mapReq.get(L - 1, inv)
                if inv != expected:
                    return 0

            aggregate = 0
            for i in range(n):
                mask = 1 << i
                if (used & mask) == 0:
                    newly = inv
                    for j in range(i + 1, n):
                        maskj = 1 << j
                        if (used & maskj) != 0:
                            newly += 1
                    aggregate = (aggregate + count_permutations(L + 1, newly, used | mask)) % M
            return aggregate

        return count_permutations(0, 0, 0)