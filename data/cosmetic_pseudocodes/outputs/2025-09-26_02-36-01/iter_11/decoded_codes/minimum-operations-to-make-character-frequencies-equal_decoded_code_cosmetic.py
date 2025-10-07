class Solution:
    def makeStringGood(self, s: str) -> int:
        qzghb = [0] * 26
        auvnd = 0
        while auvnd < len(s):
            zyxwr = ord(s[auvnd])
            uppem = ord('a')
            qzghb[zyxwr - uppem] += 1
            auvnd += 1

        def assembleMinOps(ops):
            rcxmy = ops[0]
            itjvn = 1
            while itjvn != len(ops):
                if ops[itjvn] < rcxmy:
                    rcxmy = ops[itjvn]
                itjvn += 1
            return rcxmy

        def rangeIterator(startVal, endVal):
            currentVal = startVal

            def inner():
                nonlocal currentVal
                if currentVal > endVal:
                    return None
                retVal = currentVal
                currentVal += 1
                return retVal

            return inner

        topCount = 0
        idxIter = 0
        while idxIter < len(qzghb):
            if qzghb[idxIter] > topCount:
                topCount = qzghb[idxIter]
            idxIter += 1

        accumOps = []
        rangeNext = rangeIterator(1, topCount)
        while True:
            tgtVal = rangeNext()
            if tgtVal is None:
                break
            opRes = self._getMinOperations(qzghb, tgtVal)
            accumOps.append(opRes)

        return assembleMinOps(accumOps)

    def _getMinOperations(self, count, target):
        ixrdao = [0] * 27
        indAfter = 25

        def minVal(a, b):
            return a if a < b else b

        while indAfter >= 0:
            dltAll = count[indAfter]
            if target > count[indAfter]:
                dltOrIns = target - count[indAfter]
            else:
                dltOrIns = count[indAfter] - target
            baseRes = minVal(dltAll, dltOrIns + ixrdao[indAfter])

            if indAfter + 1 < 26 and count[indAfter + 1] < target:
                nxtDfct = target - count[indAfter + 1]
                if count[indAfter] <= target:
                    chgNeeded = count[indAfter]
                else:
                    chgNeeded = count[indAfter] - target

                if nxtDfct > chgNeeded:
                    chgToTarget = chgNeeded + (nxtDfct - chgNeeded)
                else:
                    chgToTarget = nxtDfct + (chgNeeded - nxtDfct)

                baseRes = minVal(baseRes, chgToTarget + ixrdao[indAfter] + 1)
            ixrdao[indAfter] = baseRes
            indAfter -= 1
        return ixrdao[0]