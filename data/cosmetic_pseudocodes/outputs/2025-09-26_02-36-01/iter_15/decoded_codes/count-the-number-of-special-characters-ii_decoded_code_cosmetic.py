class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        pOmega = {}
        pXi = {}
        kTheta = 0
        lSigma = 0
        while lSigma < len(word):
            vEpsilon = word[lSigma]
            if vEpsilon not in pOmega:
                pOmega[vEpsilon] = lSigma
            pXi[vEpsilon] = lSigma
            lSigma += 1
        rDelta = 0
        allAlphaLower = "abcdefghijklmnopqrstuvwxyz"
        allAlphaUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            if rDelta >= len(allAlphaLower):
                break
            gMu = allAlphaLower[rDelta]
            bNu = allAlphaUpper[rDelta]
            zLambda = gMu in pXi
            yKappa = bNu in pOmega
            if zLambda and yKappa and (pXi[gMu] < pOmega[bNu]):
                kTheta += 1
            rDelta += 1
        return kTheta