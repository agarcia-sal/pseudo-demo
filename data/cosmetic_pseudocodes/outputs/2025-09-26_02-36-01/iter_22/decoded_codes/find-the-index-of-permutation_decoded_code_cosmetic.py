class Solution:
    def getPermutationIndex(self, perm):
        q = (10 ** 9) + 1
        r = len(perm)
        t = [1] * r

        s = 1
        while s < r:
            t[s] = t[s - 1] * s
            s += 1

        u = list(range(1, r + 1))

        v = 0
        w = 0
        while True:
            if w == r:
                break

            x = 0
            while True:
                if u[x] == perm[w]:
                    break
                x += 1

            v += x * t[r - w - 1]
            del u[x]

            w += 1

        return v % q