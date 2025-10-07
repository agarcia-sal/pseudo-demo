class Solution:
    def isArraySpecial(self, nums, queries):
        deltaList = []
        for val in nums:
            modVal = val - 2 * (val // 2)  # val % 2
            deltaList.append(modVal)

        accumSpecial = [0] * len(nums)
        for pos in range(1, len(nums)):
            if deltaList[pos] == deltaList[pos - 1]:
                accumSpecial[pos] = accumSpecial[pos - 1] + 1
            else:
                accumSpecial[pos] = accumSpecial[pos - 1]

        outputVals = []
        for x, y in queries:
            if x == y:
                outputVals.append(True)
            else:
                baseVal = accumSpecial[x] if x > 0 else 0
                diffCheck = accumSpecial[y] - baseVal
                outputVals.append(diffCheck == 0)

        return outputVals