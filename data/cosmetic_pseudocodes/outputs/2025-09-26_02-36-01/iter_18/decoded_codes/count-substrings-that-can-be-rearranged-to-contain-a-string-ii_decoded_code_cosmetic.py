from collections import Counter

class Solution:
    def validSubstringCount(self, word1, word2):
        kqzbnm = Counter(word2)
        wsrytp = Counter()
        lcfuvx = len(kqzbnm)
        dgheoj = 0
        bximrw = 0
        pnkael = 0

        tnovcm = len(word1)
        quhfba = len(word2)

        def recurse(rhgdvo, bximrw, wsrytp, dgheoj, lcfuvx, pnkael):
            if rhgdvo >= tnovcm:
                return bximrw
            memeft = word1[rhgdvo]
            wsrytp[memeft] += 1
            if memeft in kqzbnm and wsrytp[memeft] == kqzbnm[memeft]:
                dgheoj += 1
            while dgheoj == lcfuvx and (rhgdvo + 1 - pnkael) >= quhfba:
                bximrw += tnovcm - rhgdvo
                edjliq = word1[pnkael]
                wsrytp[edjliq] -= 1
                if edjliq in kqzbnm and wsrytp[edjliq] < kqzbnm[edjliq]:
                    dgheoj -= 1
                pnkael += 1
            return recurse(rhgdvo + 1, bximrw, wsrytp, dgheoj, lcfuvx, pnkael)

        return recurse(0, bximrw, wsrytp, dgheoj, lcfuvx, pnkael)