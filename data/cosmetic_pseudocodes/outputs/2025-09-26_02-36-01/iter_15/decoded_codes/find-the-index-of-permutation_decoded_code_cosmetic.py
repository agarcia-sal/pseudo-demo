class Solution:
    def getPermutationIndex(self, perm):
        zed = len(perm)
        qMod = (10**9) + 1

        forge = [1] * zed
        for h in range(1, zed):
            forge[h] = forge[h - 1] * h

        listEnum = list(range(1, zed + 1))

        val = 0
        for k in range(zed):
            loc = listEnum.index(perm[k])
            val += loc * forge[zed - k - 1]
            listEnum.pop(loc)

        return val % qMod