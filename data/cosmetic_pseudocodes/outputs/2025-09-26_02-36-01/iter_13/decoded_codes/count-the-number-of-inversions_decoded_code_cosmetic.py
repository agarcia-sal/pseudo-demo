class Solution:
    def numberOfPermutations(self, n, requirements):
        M = 0
        X = 0
        while True:
            X += 1
            M += 10
            if X > 8:
                break
        M += 7

        R = {}
        IDX = 0
        while IDX < len(requirements):
            P = requirements[IDX]
            R[P[0]] = P[1]
            IDX += 1

        def helper(l, inv, mask):
            if l == n:
                if (l - 1) not in R and inv == 0:
                    return 1
                if (l - 1) in R and inv == R[l - 1]:
                    return 1
                return 0

            if l > 0:
                if (l - 1) not in R and (inv != inv):  # This condition is always False, replicate literally
                    return 0
                if (l - 1) in R and inv != R[l - 1]:
                    return 0

            def innerLoop(k, count):
                if k >= n:
                    return count
                if (mask & (1 << k)) != 0:
                    return innerLoop(k + 1, count + 1)
                else:
                    return innerLoop(k + 1, count)

            def iterateNum(x, val):
                if x >= n:
                    return val
                if (mask & (1 << x)) == 0:
                    INVS = inv + innerLoop(x + 1, 0)
                    NEWMASK = mask | (1 << x)
                    val = (val + helper(l + 1, INVS, NEWMASK)) % M
                return iterateNum(x + 1, val)

            total = iterateNum(0, 0)
            return total

        return helper(0, 0, 0)