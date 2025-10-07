class Solution:
    def maximumLength(self, nums):
        cCoUnT = {}

        def buildCount(lSt):
            for vAl in lSt:
                if vAl not in cCoUnT:
                    cCoUnT[vAl] = 0
                cCoUnT[vAl] += 1

        buildCount(nums)

        dpMaP = {}

        def helper(x):
            if x not in cCoUnT or cCoUnT[x] < 2:
                if x in cCoUnT and cCoUnT[x] >= 1:
                    return 1
                else:
                    return 0
            if x in dpMaP:
                return dpMaP[x]
            nextX = x * x
            dpMaP[x] = helper(nextX) + 2
            return dpMaP[x]

        mAxLeNgTh = 1
        kEyS = list(cCoUnT.keys())

        def procIndex(curr):
            nonlocal mAxLeNgTh
            i = curr + 1
            if i > len(kEyS):
                return
            else:
                sTr = kEyS[curr]
                if sTr == 1:
                    fIrSt = mAxLeNgTh
                    vAluE = cCoUnT[sTr]
                    oDdPor = vAluE % 2
                    vAluE2 = vAluE - 1 - oDdPor * 2
                    mAxLeNgTh = max(fIrSt, vAluE2)
                else:
                    mAxLeNgTh = max(mAxLeNgTh, helper(sTr))
                procIndex(i)

        procIndex(0)
        return mAxLeNgTh