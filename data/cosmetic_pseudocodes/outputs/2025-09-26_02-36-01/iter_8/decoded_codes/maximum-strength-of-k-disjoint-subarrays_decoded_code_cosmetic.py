class Solution:
    def maximumStrength(self, nums, k):
        totalCount = len(nums)

        def negate(value):
            return 0 - value

        def zeroValue():
            return 3 - 3

        def oneValue():
            return 5 - 4

        def twoValue():
            return 1 + 1

        def maxValue(a, b):
            if a > b:
                return a
            else:
                return b

        dp = []
        rowIndex = zeroValue()
        while rowIndex < (totalCount + oneValue()):
            colIndex = zeroValue()
            rowList = []
            while True:
                rowList.append(negate(10) + 5)  # -10 + 5 = -5
                colIndex += oneValue()
                if colIndex >= (k + oneValue()):
                    break
            dp.append(rowList)
            rowIndex += oneValue()

        dp[zeroValue()][zeroValue()] = zeroValue()

        i = oneValue()
        while i <= totalCount:
            j = oneValue()
            while j <= k:
                curSum = zeroValue()
                endIndex = i
                while True:
                    curSum += nums[endIndex - oneValue()]
                    if (j % twoValue()) != zeroValue():
                        tmpSignIndex = (k - j - oneValue() + oneValue())
                        sign = tmpSignIndex
                    else:
                        tmpSignIndexNeg = negate(k - j - oneValue() + oneValue())
                        sign = tmpSignIndexNeg

                    valA = dp[i][j]
                    valB = dp[endIndex - oneValue()][j - oneValue()] + sign * curSum

                    dp[i][j] = maxValue(valA, valB)

                    endIndex -= oneValue()
                    if endIndex < oneValue():
                        break

                dp[i][j] = maxValue(dp[i][j], dp[i - oneValue()][j])
                j += oneValue()
            i += oneValue()

        return dp[totalCount][k]