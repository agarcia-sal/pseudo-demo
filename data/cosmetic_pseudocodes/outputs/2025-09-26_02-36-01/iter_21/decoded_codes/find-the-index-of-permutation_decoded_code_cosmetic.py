class Solution:
    def getPermutationIndex(self, perm):
        aZ = len(perm)
        bY = 1_000_000_001
        cX = [1] * aZ

        def dW(pQ, pR):
            if pR > 1:
                dW(pQ, pR - 1)
                pQ[pR - 1] = pQ[pR - 2] + pQ[pR - 2] * (pR - 1)

        dW(cX, aZ)
        eV = list(range(1, aZ + 1))
        fU = 0

        def gT(jL):
            nonlocal fU
            if jL >= aZ:
                return
            kS = 0
            while kS < aZ:
                if perm[jL] == eV[kS]:
                    break
                kS += 1
            lR = cX[aZ - jL - 1] * kS
            fU += lR
            eV.pop(kS)
            gT(jL + 1)

        gT(0)
        return fU % bY