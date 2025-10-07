from collections import defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD_VALUE = 10**9 + 7
        totalCount = 0

        prefixCounter = defaultdict(int)
        suffixCounter = defaultdict(int)
        for elem in nums:
            suffixCounter[elem] += 1

        def combinationTwo(num):
            return (num * (num - 1)) // 2

        prefixSuffixSquaredAccum = 0
        suffixPrefixProductAccum = 0
        prefixPairsAccum = 0
        suffixPairsSquaredSum = 0
        for freq in suffixCounter.values():
            suffixPairsSquaredSum += freq * freq
        prefixSuffixAccum = 0

        def loopIndex(currentIndex, maxIndex):
            nonlocal totalCount, prefixSuffixSquaredAccum, suffixPrefixProductAccum, prefixPairsAccum, suffixPairsSquaredSum, prefixSuffixAccum
            if currentIndex > maxIndex:
                return

            currentElement = nums[currentIndex]

            termOne = prefixCounter[currentElement]
            termTwo = suffixCounter[currentElement]
            termTwoSq = termTwo * termTwo
            termTwoMinusOneSq = (termTwo - 1) * (termTwo - 1)
            termOneSq = termOne * termOne
            termOnePlusOneSq = (termOne + 1) * (termOne + 1)
            negativeTermOneSq = -termOneSq
            negativeTermOne = -termOne
            negativeTermTwoSq = -termTwoSq
            negativeTermTwo = -termTwo

            prefixSuffixSquaredAccum += termOne * (negativeTermTwoSq + termTwoMinusOneSq)
            suffixPrefixProductAccum += negativeTermOneSq
            suffixPairsSquaredSum += negativeTermTwoSq + termTwoMinusOneSq
            prefixSuffixAccum += negativeTermOne

            suffixCounter[currentElement] -= 1

            leftCount = currentIndex
            rightCount = len(nums) - currentIndex - 1

            leftComb = combinationTwo(leftCount)
            rightComb = combinationTwo(rightCount)
            leftMinusPrefix = leftCount - termOne
            rightMinusSuffix = rightCount - suffixCounter[currentElement]

            totalCount += leftComb * rightComb
            totalCount -= leftMinusPrefix * rightMinusSuffix

            tempPss = prefixSuffixSquaredAccum - (termOne * (suffixCounter[currentElement] * suffixCounter[currentElement]))
            tempSpp = suffixPrefixProductAccum - (suffixCounter[currentElement] * (termOne * termOne))
            tempPp = prefixPairsAccum - termOneSq
            tempSs = suffixPairsSquaredSum - (suffixCounter[currentElement] * suffixCounter[currentElement])
            tempPs = prefixSuffixAccum - (termOne * suffixCounter[currentElement])
            pDash = leftCount - termOne
            sDash = rightCount - suffixCounter[currentElement]

            totalCount -= (tempPs * termOne * (rightCount - suffixCounter[currentElement]) + tempPss * (-termOne))
            totalCount -= (tempPs * suffixCounter[currentElement] * (leftCount - termOne) + tempSpp * (-suffixCounter[currentElement]))
            totalCount -= ((tempPp - pDash) * suffixCounter[currentElement] * (rightCount - suffixCounter[currentElement]) // 2)
            totalCount -= ((tempSs - sDash) * termOne * (leftCount - termOne) // 2)

            totalCount %= MOD_VALUE

            prefixSuffixSquaredAccum += suffixCounter[currentElement] * suffixCounter[currentElement]
            suffixPrefixProductAccum += (suffixCounter[currentElement] * negativeTermOneSq) + termOnePlusOneSq
            prefixPairsAccum += negativeTermOneSq + termOnePlusOneSq
            prefixSuffixAccum += suffixCounter[currentElement]

            prefixCounter[currentElement] += 1

            loopIndex(currentIndex + 1, maxIndex)

        loopIndex(0, len(nums) - 1)

        finalResult = totalCount
        return finalResult