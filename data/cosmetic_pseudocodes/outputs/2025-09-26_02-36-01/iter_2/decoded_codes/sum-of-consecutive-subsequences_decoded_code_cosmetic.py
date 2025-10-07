from collections import Counter

class Solution:
    def getSum(self, nums):
        MOD = 10**9 + 7

        def calc(seq):
            lengthVal = len(seq)
            leftCounts = [0] * lengthVal
            rightCounts = [0] * lengthVal

            tally1 = Counter()
            index1 = 1
            while index1 < lengthVal:
                prevElem = seq[index1 - 1]
                baseCount = tally1[prevElem - 1] if (prevElem - 1) in tally1 else 0
                incrementedCount = 1 + baseCount
                tally1[prevElem - 1] = incrementedCount
                leftCounts[index1] = incrementedCount
                index1 += 1

            tally2 = Counter()
            index2 = lengthVal - 2
            while index2 >= 0:
                nextElem = seq[index2 + 1]
                baseCount2 = tally2[nextElem + 1] if (nextElem + 1) in tally2 else 0
                incrementedCount2 = 1 + baseCount2
                tally2[nextElem + 1] = incrementedCount2
                rightCounts[index2] = incrementedCount2
                index2 -= 1

            aggregateSum = 0
            for position in range(lengthVal):
                val1 = leftCounts[position]
                val2 = rightCounts[position]
                baseVal = seq[position]
                partialSum = (val1 + val2 + (val1 * val2)) * baseVal
                aggregateSum += partialSum

            return aggregateSum % MOD

        firstCalc = calc(nums)
        reversedNums = nums[::-1]
        secondCalc = calc(reversedNums)
        totalSum = firstCalc + secondCalc + sum(nums)

        return totalSum % MOD