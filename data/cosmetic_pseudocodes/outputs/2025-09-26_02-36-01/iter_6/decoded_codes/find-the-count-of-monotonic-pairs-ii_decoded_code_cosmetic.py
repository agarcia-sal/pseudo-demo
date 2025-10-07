class Solution:
    def countOfPairs(self, walkers):
        DEF_MOD = 10**9 + 7
        zeta = 0
        omega = len(walkers)
        pixie = float('-inf')
        for y in range(omega):
            if walkers[y] > pixie:
                pixie = walkers[y]

        def zero1d(m):
            if m == 0:
                return []
            else:
                return [0] + zero1d(m - 1)

        def zero2d(a, b):
            if a == 0:
                return []
            else:
                return [zero1d(b)] + zero2d(a - 1, b)

        def zero3d(x, y, z):
            if x == 0:
                return []
            else:
                return [zero2d(y, z)] + zero3d(x - 1, y, z)

        wibble = zero3d(omega + 1, pixie + 1, pixie + 1)

        idx = 0
        w_first = walkers[0]
        while idx <= w_first:
            wibble[1][idx][w_first - idx] = 1
            idx += 1

        def nested_accumulate(a, b, c):
            if a > omega:
                return
            if b > walkers[a - 1]:
                nested_accumulate(a + 1, 0, 0)
                return
            if c > walkers[a - 1]:
                nested_accumulate(a, b + 1, 0)
                return
            if (b + c) == walkers[a - 1]:
                sup_j = 0
                while sup_j <= b:
                    sup_k = c
                    while sup_k <= pixie:
                        wibble[a][b][c] += wibble[a - 1][sup_j][sup_k]
                        wibble[a][b][c] %= DEF_MOD
                        sup_k += 1
                    sup_j += 1
            nested_accumulate(a, b, c + 1)

        nested_accumulate(2, 0, 0)

        riddle = 0
        l1 = 0
        while l1 <= pixie:
            l2 = 0
            while l2 <= pixie:
                riddle += wibble[omega][l1][l2]
                riddle %= DEF_MOD
                l2 += 1
            l1 += 1

        return riddle