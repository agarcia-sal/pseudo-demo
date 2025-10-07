class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        constMod = 10**9 + 7
        lengthN = len(nums)
        tableDP = [[0] * (k + 1) for _ in range(lengthN + 1)]
        tableDP[0][0] = 1

        for idxOuter in range(1, lengthN + 1):
            num = nums[idxOuter - 1]
            for idxInner in range(k + 1):
                tableDP[idxOuter][idxInner] = tableDP[idxOuter - 1][idxInner]
                if idxInner >= num:
                    tableDP[idxOuter][idxInner] = (tableDP[idxOuter][idxInner] + tableDP[idxOuter - 1][idxInner - num]) % constMod
                else:
                    tableDP[idxOuter][idxInner] %= constMod

        resultPower = 0
        limitNum = (1 << lengthN) - 1  # 2^lengthN - 1

        def bitSetCountAndSum(val: int, pos: int, accSum: int, accCount: int) -> tuple[int, int]:
            if pos == lengthN:
                return accSum, accCount
            if (val >> pos) & 1 == 1:
                return bitSetCountAndSum(val, pos + 1, accSum + nums[pos], accCount + 1)
            else:
                return bitSetCountAndSum(val, pos + 1, accSum, accCount)

        currVal = 1
        while currVal <= limitNum:
            sumSubset, countSubset = bitSetCountAndSum(currVal, 0, 0, 0)
            if sumSubset == k:
                addVal = 1 << (lengthN - countSubset)  # 2^(lengthN - countSubset)
                resultPower = (resultPower + addVal) % constMod
            currVal += 1

        return resultPower