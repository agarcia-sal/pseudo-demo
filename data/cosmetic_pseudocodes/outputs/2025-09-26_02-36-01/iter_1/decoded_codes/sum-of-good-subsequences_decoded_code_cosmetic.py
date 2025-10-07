from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        MODULUS = 1_000_000_007
        freqMap = defaultdict(int)
        sumMap = defaultdict(int)

        for num in nums:
            freqMap[num] = (freqMap[num] + 1) % MODULUS
            sumMap[num] = (sumMap[num] + num) % MODULUS

            leftFreq = freqMap.get(num - 1, 0)
            leftSum = sumMap.get(num - 1, 0)
            sumMap[num] = (sumMap[num] + leftSum + (leftFreq * num) % MODULUS) % MODULUS
            freqMap[num] = (freqMap[num] + leftFreq) % MODULUS

            rightFreq = freqMap.get(num + 1, 0)
            rightSum = sumMap.get(num + 1, 0)
            sumMap[num] = (sumMap[num] + rightSum + (rightFreq * num) % MODULUS) % MODULUS
            freqMap[num] = (freqMap[num] + rightFreq) % MODULUS

        aggregateSum = 0
        for val in sumMap.values():
            aggregateSum = (aggregateSum + val) % MODULUS

        return aggregateSum