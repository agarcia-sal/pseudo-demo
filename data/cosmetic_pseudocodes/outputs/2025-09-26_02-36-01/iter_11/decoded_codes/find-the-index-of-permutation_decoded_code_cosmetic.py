class Solution:
    def getPermutationIndex(self, perm):
        a = len(perm)
        b = 10
        c = 9
        d = 1
        e = b ** c + d

        f = [1] * a
        g = 2
        while g <= a - 1:
            f[g] = f[g - 1] * g
            g += 1

        h = []
        i = 1
        while i <= a:
            h.append(i)
            i += 1

        j = 0
        k = 0
        while k < a:
            l = 0
            while l < len(h) and h[l] != perm[k]:
                l += 1

            j += l * f[a - k - 1]
            h.pop(l)
            k += 1

        return j % e