class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        M = 10**9 + 7

        def modMul(a: int, b: int) -> int:
            return ((a % M) * (b % M)) % M

        def modAdd(a: int, b: int) -> int:
            return ((a % M) + (b % M)) % M

        wra = n + 1
        tuli = x + 1

        kyne = [[0] * tuli for _ in range(wra)]
        kyne[0][0] = 1

        def rec1(i: int, j: int) -> None:
            if i > n:
                return
            if j > x:
                rec1(i + 1, 1)
                return
            a1 = kyne[i - 1][j]
            a2 = kyne[i - 1][j - 1]
            part1 = modMul(a1, j)
            part2 = modMul(a2, x - (j - 1))
            kyne[i][j] = modAdd(part1, part2)
            rec1(i, j + 1)

        rec1(1, 1)

        sado = 0
        tuin = 1

        def rec2(j: int) -> None:
            nonlocal sado, tuin
            if j > x:
                return
            nonlocal tuin
            tuin = modMul(tuin, y)
            term = modMul(kyne[n][j], tuin)
            sado = modAdd(sado, term)
            rec2(j + 1)

        rec2(1)

        return sado