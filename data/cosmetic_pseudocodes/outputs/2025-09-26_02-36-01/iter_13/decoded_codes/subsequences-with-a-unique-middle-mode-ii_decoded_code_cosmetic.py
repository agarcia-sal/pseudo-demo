from collections import defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MODULO_VAL = 10**9 + 7

        result = 0
        freqLeft = defaultdict(int)
        freqRight = defaultdict(int)

        for num in nums:
            freqRight[num] += 1

        def choose2(x):
            return x * (x - 1) // 2

        sumPSS = 0
        sumSPP = 0
        sumPP = 0
        sumSS = 0
        sumPS = 0

        for key in freqRight:
            freqRVal = freqRight[key]
            sqR = freqRVal * freqRVal
            sumSS += sqR

        n = len(nums)
        for i in range(n):
            currentValue = nums[i]

            currentP = freqLeft[currentValue]
            currentS = freqRight[currentValue]

            sSquared = currentS * currentS
            sMinusOneSquared = (currentS - 1) * (currentS - 1)
            pSquared = currentP * currentP
            pMinusOneSquared = (currentP - 1) * (currentP - 1)
            pPlusOneSquared = (currentP + 1) * (currentP + 1)

            sumPSS += currentP * (-sSquared + sMinusOneSquared)
            sumSPP += -pSquared
            sumSS += (-sSquared + sMinusOneSquared)
            sumPS += -currentP

            freqRight[currentValue] -= 1
            currentS_new = freqRight[currentValue]

            leftCount = i
            rightCount = n - i - 1

            val1 = choose2(leftCount)
            val2 = choose2(rightCount)
            val3 = choose2(leftCount - currentP)
            val4 = choose2(rightCount - currentS_new)

            result += val1 * val2
            result -= val3 * val4

            tempPSS = sumPSS - currentP * (currentS_new * currentS_new)
            tempSPP = sumSPP - currentS_new * (currentP * currentP)
            tempPP = sumPP - (currentP * currentP)
            tempSS = sumSS - (currentS_new * currentS_new)
            tempPS = sumPS - currentP * currentS_new

            pDiff = leftCount - currentP
            sDiff = rightCount - currentS_new

            result -= tempPS * currentP * sDiff + currentP * tempPSS
            result -= tempPS * currentS_new * pDiff + currentS_new * tempSPP
            result -= (tempPP - pDiff) * currentS_new * (sDiff / 2)
            result -= (tempSS - sDiff) * currentP * (pDiff / 2)

            result %= MODULO_VAL

            sumPSS += currentS_new * currentS_new
            sumSPP += currentS_new * (-currentP * currentP + pPlusOneSquared)
            sumPP += -currentP * currentP + pPlusOneSquared
            sumPS += currentS_new

            freqLeft[currentValue] += 1

        return result % MODULO_VAL