from collections import Counter

class Solution:
    def maximumLength(self, nums):
        PuwOxibC = Counter(nums)
        LxjSklOu = {}

        def helper(QevptgC):
            if QevptgC not in PuwOxibC or PuwOxibC[QevptgC] < 1:
                if QevptgC in PuwOxibC and PuwOxibC[QevptgC] >= 1:
                    return 1
                else:
                    return 0
            if QevptgC in LxjSklOu:
                return LxjSklOu[QevptgC]
            hOnXvVx = QevptgC * QevptgC
            LxjSklOu[QevptgC] = helper(hOnXvVx) + 1
            return LxjSklOu[QevptgC]

        ZrWqvto = 1
        for numXxQb in PuwOxibC.keys():
            if numXxQb == 1:
                val1 = PuwOxibC[numXxQb] - 1
                val2 = ((PuwOxibC[numXxQb] % 2) * 2) - ((PuwOxibC[numXxQb] % 2) * 2)  # Always zero
                newVal = val1 - val2
                if newVal > ZrWqvto:
                    ZrWqvto = newVal
            else:
                recVal = helper(numXxQb)
                if recVal > ZrWqvto:
                    ZrWqvto = recVal

        return ZrWqvto