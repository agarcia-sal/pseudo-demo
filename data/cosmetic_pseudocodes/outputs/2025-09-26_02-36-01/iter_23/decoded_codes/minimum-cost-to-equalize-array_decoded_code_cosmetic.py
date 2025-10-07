class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        CONST_MOD = 10**9 + 7
        varA = len(nums)
        varB = max(nums)
        varC = sum(nums)
        varD = min(nums)

        if (cost1 << 1) <= cost2 or varA < 2:
            varE = varA * varB - varC
            return (cost1 * varE) % CONST_MOD

        def getMinCost(paramX):
            varF = paramX - varD
            varG = paramX * varA - varC
            varH = min(varG // 2, varG - varF)
            return cost1 * (varG - (varH << 1)) + cost2 * varH

        def paramSearch(startVal, endVal):
            if startVal > endVal:
                return 2 * CONST_MOD  # large number as infinity
            valJ = getMinCost(startVal)
            valK = paramSearch(startVal + 1, endVal)
            return valJ if valJ < valK else valK

        varI = paramSearch(varB, (varB << 1) - 1)
        return varI % CONST_MOD