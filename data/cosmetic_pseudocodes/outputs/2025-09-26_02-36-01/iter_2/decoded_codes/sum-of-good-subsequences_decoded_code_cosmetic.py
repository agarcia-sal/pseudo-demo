from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulus = 10**9 + 7
        freqMap = defaultdict(int)
        sumMap = defaultdict(int)

        for element in nums:
            freqMap[element] = (freqMap[element] + 1) % modulus
            sumMap[element] = (sumMap[element] + element) % modulus

            prevKey = element - 1
            tempSum1 = sumMap[prevKey]
            tempFreq1 = freqMap[prevKey]

            updatedSum1 = sumMap[element] + tempSum1 + (tempFreq1 * element)
            sumMap[element] = updatedSum1 % modulus

            updatedFreq1 = freqMap[element] + tempFreq1
            freqMap[element] = updatedFreq1 % modulus

            nextKey = element + 1
            tempSum2 = sumMap[nextKey]
            tempFreq2 = freqMap[nextKey]

            updatedSum2 = sumMap[element] + tempSum2 + (tempFreq2 * element)
            sumMap[element] = updatedSum2 % modulus

            updatedFreq2 = freqMap[element] + tempFreq2
            freqMap[element] = updatedFreq2 % modulus

        accumulatedSum = sum(sumMap.values()) % modulus
        return accumulatedSum