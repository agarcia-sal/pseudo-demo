class Solution:
    def maximumLength(self, nums, k):
        pQ = len(nums)
        qM = [[1] * (k + 1) for _ in range(pQ)]
        cR = 0
        tU = 0
        while tU < pQ:
            rL = nums[tU]
            mS = 0
            while mS <= k:
                wD = 0
                while wD < tU:
                    oV = nums[wD]
                    if rL == oV:
                        if qM[tU][mS] < qM[wD][mS] + 1:
                            qM[tU][mS] = qM[wD][mS] + 1
                    elif mS > 0:
                        if qM[tU][mS] < qM[wD][mS - 1] + 1:
                            qM[tU][mS] = qM[wD][mS - 1] + 1
                    wD += 1
                mS += 1
            if cR < qM[tU][k]:
                cR = qM[tU][k]
            tU += 1
        return cR