class Solution:
    def makeStringGood(self, s: str) -> int:
        a0 = [0] * 26
        j4 = 0
        while j4 < len(s):
            W7 = ord(s[j4]) - ord('a')
            a0[W7] += 1
            j4 += 1

        pR = a0[0]
        hasBeenSet = False
        Ev = pR

        def _minVal(x, y):
            return x if x < y else y

        def _callForTarget(targ):
            return self._getMinOperations(a0, targ)

        def helperMax(lst):
            maxVal = lst[0]
            idxTemp = 1
            while idxTemp < len(lst):
                if lst[idxTemp] > maxVal:
                    maxVal = lst[idxTemp]
                idxTemp += 1
            return maxVal

        maxCount = helperMax(a0)
        k9 = 1
        while k9 <= maxCount:
            Rn = _callForTarget(k9)
            if not hasBeenSet:
                Ev = Rn
                hasBeenSet = True
            else:
                Ev = _minVal(Ev, Rn)
            k9 += 1
        return Ev

    def _getMinOperations(self, count, target):
        def _minVal(a, b):
            return a if a < b else b

        Gz = [0] * 27
        wP = 25
        while wP >= 0:
            d2 = count[wP]
            if target > count[wP]:
                dx = target - count[wP]
            else:
                dx = count[wP] - target

            Lr = _minVal(d2, dx + Gz[wP + 1])

            if wP + 1 < 26 and count[wP + 1] < target:
                y1 = target - count[wP + 1]
                if count[wP] <= target:
                    mV = count[wP]
                else:
                    mV = count[wP] - target

                if y1 > mV:
                    Gv = mV + (y1 - mV)
                else:
                    Gv = y1 + (mV - y1)

                Lr = _minVal(Lr, Gv + Gz[wP + 2])
            Gz[wP] = Lr
            wP -= 1
        return Gz[0]